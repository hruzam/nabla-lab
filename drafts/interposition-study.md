# AI-CLI INTERPOSITION — Loop II Résumé

*How to wrap a vendor CLI for live message access while staying a standard
customer, and how to build it to survive whatever the vendor does next.*
*Policy wording verified June 2026; treat it as the most volatile section.*
*Companion to `terminal-onion-study.md` (the substrate map).*

---

## 0. The goal, one line

> Personal access to the **living message exchange** of an AI CLI —
> driven from files, not the UI; without breaking I/O; without being billed or
> seen as an SDK agent builder. Extend, don't violate.

---

## 1. Vendor app ≠ SDK → the verb is *interpose*

You don't **link** these tools and call their functions. They are vendor
**applications**, not libraries. So you **interpose** — wedge code between two
rings of a binary you don't own. The onion gives a seam at almost every ring.

| Ring | Seam | Buys | Cost |
|---|---|---|---|
| **1** | **MCP server** (JSON-RPC / stdio) | hand the agent a new tool | none — a contract |
| **1** | **Hooks** (PreToolUse / PostToolUse / Stop) | intercept/rewrite a command pre-run | none — sanctioned |
| **6** | **`$PATH` shadow** wrapper | env/arg munging, logging | crude, zero-dep |
| **3–4** | **PTY wrap** (tmux / Zellij / `portable-pty`) | *become its terminal*: inject input, tee output, multiplex | language-agnostic, binary untouched |
| **7** | **`NODE_OPTIONS=--require`** | patch `https`/`fs`/`child_process` at load | brittle vs updates, ToS exposure |
| **7** | **network proxy** (mitmproxy + `NODE_EXTRA_CA_CERTS`) | sit on the API stream | uses app's own proxy plumbing |
| **7** | **`LD_PRELOAD`** | shim `connect`/`write`/`openat` at libc | max power, max fragility |

**Principle: stay shallow.** Ring 1 survives updates because it's a contract,
not a hack. Drop to ring 4 only to own the stream itself; ring 7 only to bend
runtime behavior — and pay the fragility tax knowingly.

---

## 2. The chosen architecture — file-backed loop around the unmodified CLI

Wrap the **interactive** binary in a PTY you own. Feed it from a file, tee its
output to a file. The binary is never patched; it can't tell your pseudo-terminal
from hardware — that's the whole point of a PTY.

```sh
tmux new -s ai claude                         # interactive, subscription auth, PTY tmux owns
tmux pipe-pane -t ai -o 'cat >> ~/ai/out.log' # READ: tee the living exchange (copy, not divert)

# WRITE: your "leaking markdown" loop — append to feed.md, it streams in as keystrokes
tail -F feed.md | while IFS= read -r line; do
  tmux send-keys -t ai -l "$line"; tmux send-keys -t ai Enter
done
# multi-line block instead: tmux load-buffer msg.md && tmux paste-buffer -t ai
```

**Why the PTY is mandatory, not optional:** interactive Claude Code is an Ink
TUI in raw mode — it needs a **TTY** on stdin. A bare `cat file | claude` fails
(`isatty()` → false). The PTY supplies the TTY, so your file bytes arrive *as
keystrokes*. I/O stays intact (you tee, you don't intercept-and-drop); the pane
renders normally; no SDK, no API key, no `-p`.

---

## 3. The unskinned terminal (why this is principled, not a hack)

The GUI emulator is **only a skin** — a userspace rasterizer. Strip it and the
terminal the kernel itself provides remains:

- **Virtual / framebuffer console** — `Ctrl+Alt+F3` → `/dev/tty3`; the kernel
  draws glyphs to the framebuffer via `fbcon`, no emulator in the path.
- **Serial console** — `/dev/ttyS0`; the terminal is literally UART bytes on a
  wire. The most "on the iron." (`console=ttyS0,115200`, `picocom`.)
- Enumerate: `cat /proc/consoles`, `ls -l /dev/tty*`.

A **PTY (`/dev/pts/N`) is the software emulation of exactly that wire.** So:

```
hardware skin:  keyboard+monitor ↔ VT/serial ↔ kernel TTY ↔ process
emulator skin:  alacritty        ↔ PTY       ↔ kernel TTY ↔ process
YOUR skin:      feed.md+out.log   ↔ PTY(tmux) ↔ kernel TTY ↔ claude
```

You aren't tapping the terminal — **you built your own unskinned front-end.**
The VT renders to a framebuffer, the emulator to pixels, *you to a markdown
file.* Same wire, interchangeable skin. Stripped to the iron, a terminal is just
**a TTY + a line discipline**; everything above is a chosen skin over one byte
contract.

---

## 4. The policy green zone  *(verified June 2026 — volatile)*

- The **Consumer Terms prohibit automated/non-human access** (bot, script) —
  **except** via an Anthropic API key, **or** where explicitly permitted.
- **Claude Code is built for scripted/automated use**, so the official product
  is itself the permitted vehicle. The operative phrase for limits:
  **"ordinary, individual usage of Claude Code."**
- **The bright line:** your subscription login (**OAuth token**) is allowed
  **only inside Claude Code and Claude.ai.** Feeding that token to the **Agent
  SDK or any other tool/service is a violation** of the Consumer Terms. (This is
  what the Feb 2026 authentication-policy update was written to stop.)
- **Scale/purpose caveat:** "ordinary individual" = personal. Always-on,
  business, or multi-user → switch to **API keys under the Commercial Terms.**

**Where this loop lands:** the tmux file-feed drives the *official interactive
product's own input*, on *subscription auth*, *single-user, personal*. The token
never leaves Claude Code. → **green.** The only grey edge is turning it
always-on / shared / commercial. Pull the verbatim ToS text before relying on it
for anything beyond personal use.

---

## 5. Codebase reality — nothing to fork, nothing to rebuild

- **No vendor source needed.** You wrap the binary as a black box; the PTY means
  you never touch its insides. (Source *did* leak 2026-03-31 and an open toolkit
  exists — **unnecessary** here.)
- **No terminal to build.** PTY, TTY, line discipline are already in the Linux
  kernel — open, and consumed *through tmux*. You don't write them.
- **What you build from scratch:** ~20–40 lines of glue — the tmux wrapper, the
  `tail -F` feeder, the output tee. Small because the kernel and tmux do the
  heavy lifting. A thin file-skin, not a terminal.

---

## 6. Resilience against vendor shifts

Bind to the most stable contract; lock all vendor specifics behind one swappable
piece. Depth of contract = number of shifts survived.

- **Spine — files are the contract.** Input file in, output log out. Invariant
  whether the backend is a terminal, an API, or a future closed GUI (the GUI
  still does message-in/response-out underneath).
- **Seam — one thin ADAPTER** holds every vendor detail (flags, auth, escape
  parsing, paths). Nothing else knows the vendor exists. A shift → rewrite one
  file; **blast radius stops there.** Today's tmux/markdown loop *is* today's
  adapter — the seam is already in the right place.
- **Keep multiple adapters ready:**
  - *interactive-CLI* — cheap (subscription), but scrapes a moving UI → fragile to parse.
  - *API* — metered, but always available and clean to parse.
  - *screen-automation* — worst-case full black-box GUI.
  Same files in the middle; swap the backend. Never stranded.
- **Canary — a tripwire (the "notice" half).** A smoke test feeds a known input
  through the adapter and checks the output shape. The instant the vendor changes
  the shape (new prompt, changed escapes, a refused pipe) it **fails loud** —
  you learn immediately, not three days into producing garbage.

**Two honest limits:**
1. **No free lunch.** Cheap path = scraping a UI that moves constantly (fragile);
   clean-parse path = the metered one. The adapter lets you *choose per job* —
   it doesn't erase the tradeoff.
2. **Portability, not immunity.** Architecture protects you from *the contract
   changing*. It cannot protect you from a vendor turning *adversarial* or
   repricing — the economics stay theirs to set.

**Keep it lean:** one seam, one canary, a couple of adapters. A giant
"just-in-case" plugin framework is the Rube Goldberg machine we reject. Files +
adapter + tripwire ≈ 90% of the resilience for almost none of the bloat.

---

## 7. OPEN BRANCH — parallel-finger daemon  *(seed for next thread)*

Code that touches the same process data as additional parallel "fingers."
Splits along the §4 line:

- **Worthy — fingers at the DISK layer.** `inotifywait` on
  `~/.claude/projects/*.jsonl`, parse each new line, react / index / append to
  *your own* anchor files. Touches the process data **without touching the
  process.** Green, file-backed, observe-and-react only; survives shifts while
  session files are written.
- **Trap — fingers hardcoded into the RUNTIME.** `NODE_OPTIONS` preload /
  in-process patch → mutate the live exchange in real time. Powerful, but fights
  the minified build, breaks on daily releases, and drifts toward the
  credential/automation violation once it acts autonomously. **Don't hardcode now.**
- **Division of labor:** **read-side fingers at the disk; write-side injection
  at the `feed.md` → PTY seam.** Observe at the file, inject at the wire. Another
  module hanging off the file contract.

---

## 8. Principle, restated

```
Vendor app ≠ SDK        → interpose, don't link
Stay shallow            → the contract is the bulletproof ring
PTY = the wire          → a file-skin is as valid as a pixel-skin
Files are the spine     → adapter swaps the backend, canary catches the shift
Green zone              → official CLI + subscription auth + personal scale
Resonance in streams.   Truth in files.
```
