#!/usr/bin/env python3
"""
brick1.py — the smallest duplex loop that proves it.

One CLI (Claude Code) in a tmux-owned PTY, interactive, on your subscription.
The bus writes a task in; the live agent in the saddle processes it; a per-turn
sentinel tells the bus "the reply landed, the turn is done"; the pane is teed to
a log. No API key. No `-p`. No SDK. No Gemma, no routing — just the duplex loop,
proven to acknowledge itself, on the cheap path.

Channel placement (per the maxim — truth in files, resonance in streams):
    live exchange  -> STREAM    (tmux PTY: send -> agent notices -> reply streams)
    the record     -> FILE      (pipe-pane tee -> ~/.bus/pane.log)
    acknowledgment -> SENTINEL  (unique per-turn token the agent echoes last)

What this PROVES: send, the agent notices, it works, it replies, and the bus
KNOWS the reply is here — without trusting, without guessing, without a meter.

What this does NOT solve (on purpose): clean reply-TEXT extraction from a
redrawn TUI is messy. Brick 1 returns the ANSI-stripped slice so you can SEE how
messy. That mess is the honest motivation for the ACP adapter (brick N), where
the reply arrives as structured data with a free completion signal.

-------------------------------------------------------------------------------
SETUP (do this once):
    1. Have Claude Code installed and logged in on your subscription
       (no ANTHROPIC_API_KEY in the environment -> subscription auth).
    2. cd into your project dir and run `claude` ONCE by hand to clear the
       first-run trust / onboarding prompts. Quit it.
RUN:
    python3 brick1.py                      # smoke test: "confirm you're live"
    python3 brick1.py "summarise ./README" # a real task
WATCH (optional, satisfying):
    tmux attach -t bus                     # see the live pane the bus is driving
TEARDOWN:
    python3 -c "import brick1; brick1.stop()"
-------------------------------------------------------------------------------
"""

import os
import re
import sys
import time
import uuid
import shlex
import tempfile
import subprocess
from pathlib import Path

SESSION = "bus"                                  # tmux session name
AGENT   = "claude"                               # interactive, subscription auth
LOG     = Path.home() / ".bus" / "pane.log"      # the record (truth, file)
POLL    = 0.2                                     # seconds between log reads
TIMEOUT = 300                                     # max seconds to wait for a turn

# Strip ECMA-48 escape sequences (CSI + two-char escapes) so we can scan text.
ANSI = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")


def _tmux(*args):
    """Run a tmux command, raising on failure."""
    return subprocess.run(("tmux", *args), check=True,
                          capture_output=True, text=True)


def _alive():
    return subprocess.run(("tmux", "has-session", "-t", SESSION),
                          capture_output=True).returncode == 0


def start():
    """Idempotently bring up the detached session and (re)attach the tee."""
    LOG.parent.mkdir(parents=True, exist_ok=True)
    if not _alive():
        # `unset ANTHROPIC_API_KEY; exec claude` guarantees subscription auth
        # in the pane regardless of how tmux inherited its environment.
        launch = f"unset ANTHROPIC_API_KEY; exec {AGENT}"
        _tmux("new-session", "-d", "-s", SESSION, "-x", "220", "-y", "50", launch)
        time.sleep(2.0)                          # let the TUI boot
    # Re-arm the pipe: no-command closes any existing pipe, then open fresh.
    # `cat >>` appends, so the log (and our byte offsets) stay valid.
    _tmux("pipe-pane", "-t", SESSION)
    _tmux("pipe-pane", "-t", SESSION, f"cat >> {shlex.quote(str(LOG))}")
    return SESSION


def _inject(text):
    """Paste a block as a bracketed paste (newline-safe), then submit."""
    with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
        f.write(text)
        buf = f.name
    try:
        _tmux("load-buffer", buf)
        _tmux("paste-buffer", "-t", SESSION, "-p", "-d")   # -p bracketed, -d drop buffer
        time.sleep(0.2)
        _tmux("send-keys", "-t", SESSION, "Enter")         # submit the turn
    finally:
        os.unlink(buf)


def ask(task, timeout=TIMEOUT):
    """Duplex call: send `task`, block until the turn completes, return the
    ANSI-stripped slice of pane output produced during the turn.

    Raises TimeoutError if the completion marker never appears.
    """
    start()
    nonce  = uuid.uuid4().hex[:12]
    marker = f"<<<TURN_DONE:{nonce}>>>"

    # The acknowledgment contract. Unique per turn, so a stale marker from a
    # previous turn in the log can never false-trigger this one.
    instruction = (f"When you have completely finished this turn, output this "
                   f"exact line and nothing after it: {marker}")
    framed = f"{task}\n\n{instruction}"

    # Read only what arrives AFTER we inject, by remembering the log size now.
    start_offset = LOG.stat().st_size if LOG.exists() else 0
    _inject(framed)

    deadline = time.time() + timeout
    last = ""
    while time.time() < deadline:
        time.sleep(POLL)
        with open(LOG, "rb") as fh:
            fh.seek(start_offset)
            clean = ANSI.sub("", fh.read().decode("utf-8", "replace"))
        if marker in clean:                                # <-- the bus KNOWS
            reply = clean.split(marker, 1)[0]
            return _tidy(reply, instruction)
        last = clean
    raise TimeoutError(
        f"no completion marker after {timeout}s\n"
        f"--- last 1500 chars of de-escaped pane ---\n{last[-1500:]}")


def _tidy(reply, instruction):
    """Best-effort de-noising of the scraped TUI. NOT clean — that's the point."""
    reply = reply.replace(instruction, "")
    lines = [ln.rstrip() for ln in reply.splitlines() if ln.strip()]
    # collapse consecutive identical lines left behind by redraw frames
    out = []
    for ln in lines:
        if not out or out[-1] != ln:
            out.append(ln)
    return "\n".join(out).strip()


def stop():
    if _alive():
        _tmux("kill-session", "-t", SESSION)


if __name__ == "__main__":
    task = " ".join(sys.argv[1:]) or \
        "Reply with one short sentence confirming you are live, then stop."
    print(f"[bus] -> {task!r}", file=sys.stderr)
    t0 = time.time()
    reply = ask(task)
    print(f"[bus] turn acknowledged in {time.time() - t0:.1f}s\n"
          f"[bus] --- raw reply slice (expect noise) ---", file=sys.stderr)
    print(reply)
