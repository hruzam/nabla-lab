# card.008 — adopt `driven` mode (bus third mode) + smoke-test brick2

`DELIVERY TARGET (amended per majkee 2026-07-07): subai is reshaping `_bus/inbox` onto the standard`
`project mail pattern (_mail/{inbox,archive}) — drop this file into subai's _mail inbox once the`
`reshape lands (or _bus/inbox meanwhile). Oraculum is deny-ruled outside nabla-lab, correctly.`
`from: @Oraculum (nabla-lab) · 2026-07-07 · WRITTEN IN RUSH — Fable sunset at midnight`
`status: ADOPTION GAVELED (G8, majkee, 2026-07-07) · always-on = DEFER (G9) · integrate via Houston at leisure`

## What arrived

nabla-lab shaped two artifacts for this project (all three gates passed 2026-07-07 — Epoch, Color,
Janus REVISE→applied; Gate-3 co-signed + crossed to papers/ same day, gavel G7):

- `/home/hruzam/nabla-lab/papers/card.interposition-driven-mode.2026-07-07.md` — instrument card
- `/home/hruzam/nabla-lab/shaped/seed.brick2.py` — runnable seed, stdlib only

## Why it matters here

The bus has `living` (card drop, **no acknowledgment**) and `worker` (`-p` — **metered against the
Agent SDK credit pool since 2026-06-15**; verify against billing, this inverts the cheap-path
assumption). `driven` is the missing middle: a persistent interactive `claude` in a per-project
tmux pane, subscription-native, with **verified completion**. Channel algebra: write at the wire
(tmux bracketed paste), read at the record — sid via SessionStart hook + `BUS_PANE` launch token,
done via Stop hook, content via transcript terminal assistant entry (nonce-correlated, keyed by
`stop_reason`). Pane scraping for acknowledgment was condemned by Color (input echo and genuine
emission indistinguishable by construction) — do not resurrect brick1's sentinel.

## Suggested integration (Houston's call, not mine)

1. **Smoke first** (~15 min): `python3 seed.brick2.py install <proj>` → `ask "confirm you are live"`.
   Settles two open questions empirically: `sid_via` report (`token` = env passthrough confirmed /
   `cwd` = doc gap real, fallback engaged) and first-inject readiness on a fresh pane (Janus's
   named next-thing-that-bites).
2. If green: `bus.config.json` gains `"mode": "driven"`; Stop events flatten to pulses in the
   medium (`.` reply-landed, `!` timeout/abort). `ask()` is serial per pane; one pane per project.
3. Compliance: attended use = green. **Always-on/unattended: GAVELED DEFER (G9, 2026-07-07)** —
   attended-driven only until majkee revisits with smoke data + policy watch.

## Trail (full context for Opus-tier integration)

`nabla-lab/session/pulse.md` → `session/gavels.2026-07-07.md` → papers card →
`nabla-lab/session/research-interposition-fullrange/epoch.findings.2026-07-07.md`. Laws respected:
SEAM (hooks only, no agent-loop surgery), MEDIUM (truth in files), LIGHT (stdlib, no GPU),
PORTABILITY (vendor specifics behind one adapter seam).
