#!/usr/bin/env python3
"""
brick2.py — brick1, adjusted: the driven-mode duplex loop with STRUCTURED acknowledgment.
(revised 2026-07-07 per @Janus gate: canary grace window; TUI boot settle)

Channel algebra (the whole adjustment): WRITE at the wire, READ at the record.
    injection      -> STREAM   (tmux PTY: bracketed paste + Enter — same as brick1)
    identity       -> HOOK     (SessionStart + BUS_PANE launch token -> sid + transcript path)
    acknowledgment -> HOOK     (Stop event in ~/.bus/hooks.jsonl — fires ONLY on normal
                                main-agent completion; never on subagent stop or user interrupt)
    content        -> FILE     (transcript JSONL: nonce-correlated user record, then the
                                terminal assistant entry keyed by stop_reason != "tool_use")

Why brick1's pane sentinel is gone (Color verdict 2026-07-07): it scanned the channel it
injected into for a token it injected — input echo and genuine emission indistinguishable
by construction. Here the nonce is read back from the STRUCTURED user record we expect to
exist, so there is no echo ambiguity; completion never touches the pane at all.

Canary discipline (Janus revise 2026-07-07): the ledger (hook subprocess) and the
transcript (claude process) are TWO INDEPENDENT WRITERS. On a miss, the reader retries
within a bounded grace window (GRACE) to absorb flush/torn-line transients; only a miss
that SURVIVES the window is schema drift and fails loud. A canary that misattributes a
transient as vendor drift corrupts the exact diagnostic this design leans on.

Design facts this code leans on (verified 2026-07-07; transcript format is officially
"internal" — hence the canary):
  * hook stdin: {"hook_event_name","session_id","transcript_path","cwd",...} (snake_case)
  * transcript lines: {"parentUuid","sessionId","type":"user"|"assistant","message":{...}}
    (camelCase sessionId — different casing than hooks, deliberate here)
  * stop_reason: "tool_use" mid-turn, "end_turn" (or other non-tool_use) terminal
  * non-message line types exist (file-history-snapshot, ai-title, ...) — never trust
    "last line"; key on stop_reason
  * subagent turns live in <sid>/subagents/*.jsonl — main transcript stays clean
  * env passthrough to hooks is a DOC GAP: the hook records $BUS_PANE; if it arrives
    empty, sid mapping self-falls-back to cwd match (valid: ONE driven pane per project)

Assumptions (violating them is a caller error, not a bug):
  * one driven pane per project dir; ask() calls to the same pane are SERIAL
  * single host, local filesystem (page-cache visibility; no NFS)

FIRST SMOKE TEST — two things it settles empirically (run before trusting round-trips):
  1. sid_via report: "token" = env passthrough confirmed; "cwd" = doc gap real, fallback on.
  2. first-inject readiness: if the first paste on a fresh pane is dropped (Ink TUI not
     accepting input yet despite BOOT_SETTLE), you eat the full TIMEOUT — raise
     BOOT_SETTLE if so. (Named by @Janus as the next thing to bite.)

-------------------------------------------------------------------------------
SETUP (once per project):
    1. Claude Code installed, logged in on subscription; run `claude` once by hand
       in the project dir to clear first-run trust prompts. Quit it.
    2. python3 brick2.py install /path/to/project     # writes the hooks fragment
                                                      # into .claude/settings.local.json
RUN:
    python3 brick2.py ask "summarise ./README" /path/to/project
    python3 brick2.py ask "confirm you are live"      # project = cwd
WATCH (optional):
    tmux attach -t bus-<slug>                         # the live pane being driven
TEARDOWN:
    python3 brick2.py stop /path/to/project
INTERNAL (called by Claude Code, not by you):
    python3 brick2.py hook                            # appends hook stdin -> ledger
-------------------------------------------------------------------------------
"""

import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
import time
import uuid
from pathlib import Path

BUS_DIR = Path.home() / ".bus"
LEDGER  = BUS_DIR / "hooks.jsonl"     # every hook event, one JSON line each
PANES   = BUS_DIR / "panes"           # per-pane state: token, sid, transcript path
POLL    = 0.2                         # seconds between ledger reads
TIMEOUT = 600                         # max seconds to wait for a turn
SID_TIMEOUT = 90                      # max seconds to wait for SessionStart after spawn
BOOT_SETTLE = 2.0                     # seconds after spawn before the pane is touched
GRACE   = 2.0                         # canary grace window (two-writer transient absorber)

# stop_reason values that END a turn. "tool_use" continues it. Anything else
# (end_turn / max_tokens / stop_sequence / refusal / future values) terminates.
MIDTURN = {"tool_use"}


# ---------------------------------------------------------------- tmux plumbing

def _tmux(*args):
    return subprocess.run(("tmux", *args), check=True, capture_output=True, text=True)


def _alive(sess):
    return subprocess.run(("tmux", "has-session", "-t", sess),
                          capture_output=True).returncode == 0


def _slug(project_dir):
    return re.sub(r"[^a-zA-Z0-9]+", "-", str(project_dir)).strip("-")[-40:]


def _session(project_dir):
    return f"bus-{_slug(project_dir)}"


def _inject(sess, text):
    """Bracketed paste (newline-safe), then submit. The ONLY pane touch we make."""
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(text)
        buf = f.name
    try:
        _tmux("load-buffer", buf)
        _tmux("paste-buffer", "-t", sess, "-p", "-d")
        time.sleep(0.2)
        _tmux("send-keys", "-t", sess, "Enter")
    finally:
        os.unlink(buf)


# ------------------------------------------------------------- ledger (hook side)

def hook():
    """Hook entrypoint: append stdin JSON + $BUS_PANE to the ledger. Fast, exit 0.
    Recording BUS_PANE doubles as the empirical env-passthrough probe."""
    raw = sys.stdin.read()
    try:
        p = json.loads(raw)
    except Exception:
        p = {"_unparsed": raw[-1000:]}
    rec = {
        "ts": time.time(),
        "event": p.get("hook_event_name"),
        "session_id": p.get("session_id"),
        "transcript_path": p.get("transcript_path"),
        "cwd": p.get("cwd"),
        "source": p.get("source"),                    # SessionStart: startup|resume|...
        "bus_pane": os.environ.get("BUS_PANE", ""),   # the probe
    }
    BUS_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as fh:
        fh.write(json.dumps(rec) + "\n")


def _ledger_size():
    return LEDGER.stat().st_size if LEDGER.exists() else 0


def _ledger_events(offset):
    """Read ledger from byte offset. Torn-line discipline: parse only
    newline-terminated lines; return (new_offset, records)."""
    if not LEDGER.exists():
        return offset, []
    with open(LEDGER, "rb") as fh:
        fh.seek(offset)
        chunk = fh.read()
    cut = chunk.rfind(b"\n")
    if cut < 0:
        return offset, []
    out = []
    for line in chunk[:cut].split(b"\n"):
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except Exception:
            pass  # foreign/garbled but complete line: skip
    return offset + cut + 1, out


# ------------------------------------------------------------- pane state + sid

def _state_path(sess):
    return PANES / f"{sess}.json"


def _state_load(sess):
    p = _state_path(sess)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def _state_save(sess, state):
    PANES.mkdir(parents=True, exist_ok=True)
    _state_path(sess).write_text(json.dumps(state, indent=2), encoding="utf-8")


def start(project_dir):
    """Idempotently bring up the driven pane for a project. Returns session name."""
    pd = str(Path(project_dir).resolve())
    sess = _session(pd)
    if _alive(sess) and _state_load(sess).get("token"):
        return sess
    token = uuid.uuid4().hex
    state = {"token": token, "project_dir": pd, "ledger_off_at_spawn": _ledger_size()}
    # unset ANTHROPIC_API_KEY -> subscription auth regardless of inherited env;
    # BUS_PANE=<token> -> identity probe for the SessionStart hook.
    launch = f"unset ANTHROPIC_API_KEY; BUS_PANE={token} exec claude"
    _tmux("new-session", "-d", "-s", sess, "-c", pd, "-x", "220", "-y", "50", launch)
    time.sleep(BOOT_SETTLE)   # let the Ink TUI boot before anything touches the pane
    _state_save(sess, state)
    return sess


def _resolve_sid(sess, timeout=SID_TIMEOUT):
    """Map pane -> (session_id, transcript_path) via the SessionStart hook event.
    Primary: BUS_PANE token match. Fallback: cwd match (one pane per project).
    Reports which path worked — that answers the env-passthrough doc gap."""
    state = _state_load(sess)
    if state.get("session_id"):
        return state
    off = state.get("ledger_off_at_spawn", 0)
    deadline = time.time() + timeout
    while time.time() < deadline:
        off, recs = _ledger_events(off)
        for r in recs:
            if r.get("event") != "SessionStart":
                continue
            via = None
            if r.get("bus_pane") and r["bus_pane"] == state.get("token"):
                via = "token"
            elif not r.get("bus_pane") and r.get("cwd") == state.get("project_dir"):
                via = "cwd"   # env did NOT pass through — fallback engaged
            if via:
                state.update(session_id=r.get("session_id"),
                             transcript_path=r.get("transcript_path"), sid_via=via)
                _state_save(sess, state)
                print(f"[bus] sid={state['session_id']} via {via}"
                      f"{' (env passthrough CONFIRMED)' if via == 'token' else ' (env gap REAL: cwd fallback)'}",
                      file=sys.stderr)
                return state
        time.sleep(POLL)
    raise TimeoutError(
        f"no SessionStart within {timeout}s — hooks installed? "
        f"run: python3 {Path(__file__).name} install {state.get('project_dir', '<project>')}")


# ------------------------------------------------------------------ the duplex

def ask(project_dir, task, timeout=TIMEOUT):
    """Duplex call: inject `task`, block until the Stop hook confirms the turn,
    return clean reply text from the transcript. Raises TimeoutError with a
    diagnosis (Stop never fires on interrupt/abort — silence IS the abort signal)."""
    sess = start(project_dir)
    state = _resolve_sid(sess)
    sid, tpath = state["session_id"], state["transcript_path"]

    nonce = uuid.uuid4().hex[:12]
    framed = f"{task}\n\n[bus-nonce:{nonce}]"
    tp = Path(tpath)
    tsize_before = tp.stat().st_size if tp.exists() else 0
    off = _ledger_size()
    _inject(sess, framed)

    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(POLL)
        off, recs = _ledger_events(off)
        if any(r.get("event") == "Stop" and r.get("session_id") == sid for r in recs):
            return _reply_from_transcript(tpath, nonce)

    grew = (tp.stat().st_size if tp.exists() else 0) > tsize_before
    raise TimeoutError(
        f"no Stop event after {timeout}s for sid={sid}. "
        f"pane_alive={_alive(sess)} transcript_grew={grew}. "
        "Stop does not fire on user interrupt/abort — likely aborted, hung, or "
        "rate-limited. Attach to inspect: tmux attach -t " + sess)


def _scan_transcript(tpath, nonce):
    """One pass over the transcript. Returns (ok, text, miss_reason).
    Torn-line discipline: parse only newline-terminated lines."""
    data = Path(tpath).read_bytes()
    cut = data.rfind(b"\n")
    lines = []
    for raw in (data[:cut].split(b"\n") if cut >= 0 else []):
        raw = raw.strip()
        if not raw:
            continue
        try:
            lines.append(json.loads(raw))
        except Exception:
            continue

    ui = None
    for i, rec in enumerate(lines):            # latest match wins
        if rec.get("type") == "user" and nonce in json.dumps(rec.get("message", {})):
            ui = i
    if ui is None:
        return False, None, "nonce'd user record not found"

    texts, terminal = [], False
    for rec in lines[ui + 1:]:
        if rec.get("type") != "assistant":
            continue                            # tool_result/user + metadata lines skipped
        msg = rec.get("message") or {}
        for block in msg.get("content") or []:
            if isinstance(block, dict) and block.get("type") == "text" and block.get("text", "").strip():
                texts.append(block["text"].strip())
        sr = msg.get("stop_reason")
        if sr and sr not in MIDTURN:
            terminal = True
            break
    if not terminal:
        return False, None, "no terminal assistant entry (stop_reason) after the nonce"
    return True, "\n\n".join(texts), ""


def _reply_from_transcript(tpath, nonce, grace=GRACE):
    """CANARY with grace window (Janus revise 2026-07-07): ledger and transcript
    have two independent writers, so a miss at the instant Stop lands may be a
    flush/torn-line TRANSIENT (cure: wait one poll), not schema drift (cure: stop
    trusting the adapter). Retry within `grace`; only a surviving miss fails loud."""
    deadline = time.time() + grace
    while True:
        ok, text, reason = _scan_transcript(tpath, nonce)
        if ok:
            return text
        if time.time() >= deadline:
            raise RuntimeError(
                f"CANARY (miss survived {grace}s grace): {reason} — "
                "transcript schema drift; fail loud, do not trust this adapter.")
        time.sleep(POLL)


# -------------------------------------------------------------------- lifecycle

def install(project_dir):
    """Register SessionStart + Stop hooks -> `brick2.py hook` in the project's
    .claude/settings.local.json (personal, gitignored). Idempotent merge."""
    me = Path(__file__).resolve()
    cmd = f"python3 {shlex.quote(str(me))} hook"
    sfile = Path(project_dir).resolve() / ".claude" / "settings.local.json"
    settings = json.loads(sfile.read_text(encoding="utf-8")) if sfile.exists() else {}
    hooks = settings.setdefault("hooks", {})
    for ev in ("SessionStart", "Stop"):
        entries = hooks.setdefault(ev, [])
        already = any(h.get("command") == cmd
                      for e in entries for h in e.get("hooks", []))
        if not already:
            entries.append({"hooks": [{"type": "command", "command": cmd}]})
    sfile.parent.mkdir(parents=True, exist_ok=True)
    sfile.write_text(json.dumps(settings, indent=2) + "\n", encoding="utf-8")
    print(f"[bus] hooks registered in {sfile}", file=sys.stderr)
    print("[bus] restart any running claude session in this project to load them.",
          file=sys.stderr)


def stop(project_dir):
    sess = _session(str(Path(project_dir).resolve()))
    if _alive(sess):
        _tmux("kill-session", "-t", sess)
    sp = _state_path(sess)
    if sp.exists():
        sp.unlink()


# -------------------------------------------------------------------------- CLI

def main(argv):
    if not argv:
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "hook":
        hook()
        return 0
    if cmd == "install":
        install(rest[0] if rest else os.getcwd())
        return 0
    if cmd == "stop":
        stop(rest[0] if rest else os.getcwd())
        return 0
    if cmd == "ask":
        if not rest:
            print("usage: brick2.py ask \"<task>\" [project_dir]", file=sys.stderr)
            return 2
        task = rest[0]
        pd = rest[1] if len(rest) > 1 else os.getcwd()
        print(f"[bus] -> {task!r}", file=sys.stderr)
        t0 = time.time()
        reply = ask(pd, task)
        print(f"[bus] turn acknowledged (Stop hook) in {time.time() - t0:.1f}s", file=sys.stderr)
        print(reply)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
