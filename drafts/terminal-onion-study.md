# THE TERMINAL ONION — Study Reference

*Scope: what "the terminal" actually is, ring by ring, plus the concrete
filesystem coordinates where the bytes live and where you tap them.*
*Product facts verified against web sources, June 2026. Kernel/UNIX mechanics
are timeless — unsourced by design.*

---

## 0. The one-line thesis

> Surface tools look like GUIs. The contract is unbroken.
> **It is text all the way down, and every ring below the skin is tap-able.**

The flashy CLIs (`claude`, `gemini`, `cursor-agent`) draw nothing graphical.
They emit ANSI/VT escape sequences into a byte stream. "UI" is a projection.

---

## 1. The onion — outer skin → core

| # | Ring | What lives here | Kernel? |
|---|------|-----------------|:---:|
| 1 | **TUI / application** | `claude`, `gemini`, `vim`, `htop`, `lazygit` | — |
| 2 | **Escape-sequence protocol** | `\e[31m` red, `\e[2J` clear, `\e[?1049h` alt-screen | — |
| 3 | **Terminal emulator** | alacritty, kitty, foot, wezterm, st — turns escapes → pixels, holds PTY **primary** | — |
| 4 | **PTY pair** | the wire: `/dev/ptmx` → `/dev/pts/N` | **yes** |
| 5 | **Line discipline (`n_tty`)** | echo, backspace, Ctrl-C→SIGINT, canonical vs raw | **yes** |
| 6 | **Shell** | bash/zsh/fish — *just another tenant*; forks+execs the tool, then blocks | — |
| 7 | **Process + FD layer** | fork/exec, process table, `/proc/PID/fd/` | **yes** |
| 8 | **Core** | kernel + silicon | **yes** |

The cardinal sin: conflating **ring 3 (emulator)** with **ring 6 (shell)**.
They are different programs. The shell is not special; the kernel is.

---

## 2. The three streams

A running agent splits its I/O into three independent byte-streams. Tap each
at a different ring.

| Stream | Crosses | Tap point | Plaintext? |
|--------|---------|-----------|:---:|
| **Render** | PTY (fd 1) | `strace -e write` | yes (escapes + content) |
| **Network** | TLS socket | `strace -e sendto` / `ss` | **no** — ciphertext on the wire |
| **Disk** | filesystem | `inotifywait` / `strace -e openat` | yes — see §5 |

---

## 3. Device-node map (the PTY wire)

| Path | Role | Read it |
|------|------|---------|
| `/dev/ptmx` | PTY multiplexer — `open()` allocates a new pair, returns the **primary** fd (anonymous, held by emulator) | — |
| `/dev/pts/N` | **subsidiary** side — the program's controlling terminal; its fd 0/1/2 | `tty` prints yours |
| `/proc/PID/fd/` | symlinks per open fd; 0,1,2 → `/dev/pts/N` for an interactive proc | `ls -l /proc/PID/fd` |
| `/proc/PID/fdinfo/N` | position + flags per fd | `cat` |

```sh
tty                         # which pts am I on
ps -o pid,tty,cmd            # controlling tty per process
who                          # who is on which pts
ls -l /proc/$(pgrep -f claude)/fd   # see 0/1/2 → /dev/pts/N, plus socket fds
lsof -p $(pgrep -f claude)          # every open file + socket, one view
```

> **Honest caveat:** you cannot cleanly mirror a pts's *output* by `cat`-ing the
> node — reading `/dev/pts/N` competes with the foreground process for its
> *input*. For reliable output capture use `strace -e write`, or wrap the
> session in `script` / `ttyrec` from the start.

---

## 4. Mount table (the literal "mount points")

The kernel's own truth about what is mounted where — raw, authoritative,
plaintext.

| Command | Gives you |
|---------|-----------|
| `cat /proc/mounts` | kernel's raw mount list (= `/proc/self/mounts`) |
| `findmnt` | the mount **tree** |
| `mount \| column -t` | aligned human view |
| `df -hT` | usage + filesystem type per mount |
| `lsblk -f` | block devices + their filesystems |

**This sandbox's mounts** (concrete example of the abstraction):

| Mount | Mode | Meaning |
|-------|------|---------|
| `/mnt/user-data/uploads` | ro | inbound — files the human handed in |
| `/mnt/user-data/outputs` | rw | deliverables land here *(this file did)* |
| `/mnt/skills/public` `…/private` `…/examples` | ro | skill substrate |
| `/home/claude` | rw | scratch — **resets between tasks** (the dream state; volatile) |

---

## 5. On-disk truth (where the timeline actually lives)

Verified June 2026. Claude Code persists every session to plaintext on disk —
this is the file-based truth, not volatile amnesia.

| Path | Contents |
|------|----------|
| `~/.claude/projects/<abs-path-encoded>/<session-id>.jsonl` | full transcript: every prompt, response, tool call, command output, pasted text |
| `~/.claude/history.jsonl` | lightweight cross-session command/meta history |
| `~/.claude/settings.json` · `settings.local.json` | config |
| `~/.claude/.credentials.json` | API creds (Linux/Windows) |

**Properties that matter:**
- **JSONL = line-delimited append.** The append-only invariant is the literal
  storage format. `tail -f` it; `jq` it; `grep` it.
- **Not encrypted at rest.** OS file permissions are the only protection. A
  `.env` read or a printed credential is written into the `.jsonl`.
- **TTL, not loss.** Files older than `cleanupPeriodDays` (default **30**) are
  deleted on startup — a filter-on-read TTL. Opt out with
  `CLAUDE_CODE_SKIP_PROMPT_HISTORY`.
- Resume: `claude -c` (latest) / `claude -r <id>` (specific).

```sh
# watch the disk truth grow in real time, from another pane:
tail -f ~/.claude/projects/*/$(ls -t ~/.claude/projects/*/ | head -1)
# or trace every file the agent touches:
strace -f -p $(pgrep -f claude) -e trace=openat,write -s 256
```

---

## 6. The tap drill (watch a live agent cross the wire)

```sh
PID=$(pgrep -f claude)

# render + disk streams (escapes, content, file writes)
strace -f -p "$PID" -e trace=read,write,openat -s 8192

# network: the API socket — ESTABLISHED to api.anthropic.com:443, ciphertext
ss -tnp  | grep "$PID"
lsof -iTCP -a -p "$PID"

# to read the network plaintext you must intercept at another ring:
#   SSLKEYLOGFILE=… + Wireshark, or a proxy (mitmproxy) with the Node agent's
#   NODE_EXTRA_CA_CERTS / HTTPS_PROXY pointed at it.
```

> `strace -f` follows forks. These agents are **recursive stream multiplexers**:
> a bash tool-call spawns a *child* with its own pipes, captures that child's
> output, and re-renders it into the agent's own surface. So `-f` exposes an
> entire process-subtree's I/O — nested byte-streams folded into one render.

---

## 7. Verified product facts — June 2026

| Tool | Render stack | Status |
|------|--------------|--------|
| **Claude Code** | React + **Ink** + **Yoga** layout · **Bun** build · **npm** dist · Node 18+ | ✅ CONFIRMED |
| **Gemini CLI** | React + **Ink** | ✅ CONFIRMED (listed in Ink's own users) |
| **Cursor CLI** | runs agents in-terminal; **render stack unknown** — *not* in Ink's user list | ⚠️ PARTIAL · `[unverified]` |

**Post-cutoff notes (training-era me couldn't know):**
- **2026-03-31** — Claude Code's full TypeScript source exposed via npm source
  maps. Leak-analysis claims the Yoga layout is a ~2700-line pure-TS rewrite,
  not a C++ binding — *plausible, leak-derived, not gospel* (official framing
  says "Meta's Yoga").
- **Bloat datum:** Claude Code reserves ~**32.8 GB virtual** for the V8 heap,
  ~45% malloc fragmentation, **746 MB peak** that never releases — classic leak
  pattern. The React-in-a-terminal tax.

---

## 8. Principle, restated

```
Ring 1–2   convention   (escape sequences — a 1970s VT220 contract, unbroken)
Ring 3     pixels       (emulator — the only thing that rasterizes)
Ring 4–5   the wire     (PTY + line discipline — first place bytes are tap-able)
Ring 6     a tenant     (the shell is not special)
Ring 7–8   truth        (/proc/PID/fd — what is actually wired to what)

Resonance lives in streams.   Truth lives in files.
```
