# cmds-zen — cold-start validation (SEARCH escalation ladder)

date: 2026-07-17
what: does the `/cmd-zen SEARCH` mechanism hold from a cold start, and at what token cost?
run by: atlas-ui session; test executed by a neutral general-purpose subagent
under test: `raw.research/agent-docs/commands/cmds-zen.md` — `COMMAND: search` (lines 6–19)

## Setup

- **Cold start.** A fresh general-purpose agent, no priming about anti-blast discipline,
  given ONLY the skill file + one query. It had to derive behaviour from the skill alone.
- **It could blast.** The agent held web tools (WebSearch/WebFetch) — the war-story failure
  mode (line 32) was available to it, not fenced off.
- **Bait query:** *"current stable version of the Claude Code CLI and its most recent notable
  change."* Version-sensitive (tempts immediate internet), but with a fresh local card in RAG —
  a partial-sufficiency trap.

## Behavioral verdict: GREEN

1. **Local RAG first** — grepped `raw.research` before any web call.
2. **Sufficiency-gated** — judged RAG *partially* sufficient (version anchor present,
   notable-change absent, ~1 week stale) and stated the reason before escalating.
3. **No parallel blast** — exactly one web query, fired alone; escalated one step, stopped
   at sufficiency.

Nuance — the right subtle move: partial local hit → single targeted escalation for the missing
half → stop. The exact inverse of the line-32 war story (skip RAG, fire 4+ concurrent krakens).

## Token cost / efficiency (~approx)

**HARD (measured this run):**
- subagent tokens: **31,104**
- tool uses: **6**
- duration: **49.5 s**
- source touches: **2** (one local grep-chain + one web query), strictly sequential
- escalation depth reached: **2 of 3** (stopped before "next query")

**ESTIMATE (counterfactual — NOT run, confidence LOW):**
- war-story blast profile: 4+ concurrent krakens (2 web searches + 3 fetches); each fetch pulls
  a full page into context.
- rough token estimate: **~70–120K** (2–4× retrieval + synthesis over redundant/overlapping
  pages). Wall-clock not improved — parallel buys nothing on a single-answer query.
- efficiency delta: the ladder answered the same query at **~1/3–1/4** the token cost, no
  latency penalty for this query class.

**Read:** for single-answer version/fact queries the escalation ladder is strictly cheaper —
parallel fan-out only earns its keep on genuine multi-target work (line 12), which this was not.

**To harden the estimate:** run a paired cold agent WITHOUT the escalation rule, same query,
measure real blast tokens. Offered, not yet run.

## Open design tension surfaced (for the lab)

PINS (lines 14–19, epoch, `[DRAFT]`) vs README-taste (lines 21–26, majkee's vision): a fixed
hot-cache of anchor paths vs navigational README-first. Not resolved here — noted. See the
atlas↔majkee thread, 2026-07-17.

## Confidence

- Behavioral verdict: **HIGH** (observed tool trace).
- Token cost: **HIGH** (measured).
- Blast counterfactual: **LOW** (estimate, unrun).
