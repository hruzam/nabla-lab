# @Epoch research report
Date: 2026-07-07
Triggered by: Oraculum — AI-CLI interposition full-range design; policy/prior-art/ACP re-verification
Scope: contract-extended — interposition study; prior June-2026 stamps treated as stale

---

## Context

The study technique: wrap the interactive Claude Code CLI in a tmux-owned PTY, feed input from
files, read output — all on a subscription (Pro/Max) OAuth login. No API key, no `-p` headless,
no SDK. We drive the official interactive product. Now extending toward multi-project, persistent,
possibly unattended/always-on orchestration. Every June-2026 policy stamp below is re-verified as
of 2026-07-07.

---

## Findings — Policy (Q1)

### Q1a: Is "ordinary, individual usage" still the operative limiting phrase?

WHAT: The phrase appears in Claude subscription plan documentation as context for usage limits,
not in the formal Consumer Terms or AUP. The actual Consumer Terms (updated October 2025) use
"consumer acting wholly or mainly outside your trade, business, craft or profession." The AUP
(effective September 2025) contains no such phrase either. The subscription-level docs that
reference "ordinary, individual usage" are describing the engineering assumptions behind rate
limits — not a legally operative clause. The phrase is real but its legal weight is soft: it
explains rate-limit calibration, it is not a prohibition on anything.

SINCE when: October 2025 (Consumer Terms), September 2025 (AUP) — both predate the February 2026
enforcement wave. The phrase appears in secondary product docs, not formal legal terms.

SOURCE: https://www.anthropic.com/legal/consumer-terms (fetched 2026-07-07);
https://www.anthropic.com/legal/aup (fetched 2026-07-07);
https://autonomee.ai/blog/claude-code-terms-of-service-explained/ (fetched 2026-07-07)

CONFIDENCE: H for "the phrase is in docs but not formal terms"; M for "its operative weight is
limited to explaining rate limits."

IMPACT: The phrase is real context but does not constitute a formal prohibition on scripted or
multi-session use of the official CLI. Do not overweight it as a policy anchor.

ACTION: Do not cite "ordinary individual usage" as the operative clause in the artifact. Cite the
Consumer Terms § 3.7 exemption for "where Anthropic otherwise explicitly permits it" instead —
and Claude Code CLI qualifies as explicitly permitted.

---

### Q1b: Is the bright line still: subscription OAuth permitted ONLY inside Claude Code / Claude.ai?

WHAT: Yes, confirmed, with one structural clarification. The prohibition is on using OAuth tokens
"in any other product, tool, or service — including the Agent SDK." The bright line is token
extraction and relay — any tool that intercepts the OAuth flow and uses the token outside the
official Claude Code / Claude.ai client is banned. The official `claude` binary on any machine
(local, VPS, CI/CD) is the permitted surface. This is not a location restriction; it is an
identity restriction: the genuine Anthropic client binary, running OAuth as intended.

Formal enforcement chronology:
- January 2026: server-side blocking of third-party OAuth relay (technical enforcement)
- February 2026: policy documentation updated and clarified
- April 5, 2026: formal policy announcement — third-party agents banned from using subscription
  credentials; Claude Pro/Max restricted to direct, human-initiated use on official surfaces
- May 13 / June 15, 2026: partial reversal — Agent SDK credit pool introduced for programmatic
  use at API rates ($20 Pro / $100 Max 5x / $200 Max 20x per month)

SOURCE:
https://www.theregister.com/2026/02/20/anthropic_clarifies_ban_third_party_claude_access/ (H)
https://awesomeagents.ai/news/claude-code-oauth-policy-third-party-crackdown/ (H)
https://autonomee.ai/blog/claude-code-terms-of-service-explained/ (M)
https://groundy.com/articles/anthropic-bans-third-party-use-subscription-auth-three-stage-repricing/ (M)

CONFIDENCE: H

IMPACT: Unambiguously clean for the interposition approach. We drive the genuine `claude` binary.
No token extraction, no relay, no third-party client. Bright line not crossed.

ACTION: Document explicitly in the artifact: the PTY-interposition approach does NOT cross the
OAuth bright line because it never extracts or relays the token.

---

### Q1c: Always-on / unattended / multi-session automation driving the interactive product — permitted, grey, or prohibited?

WHAT: GREY — trending toward permitted for the interactive CLI, but with a structural ambiguity
introduced June 15, 2026.

Evidence for permitted:
- Consumer Terms § 3.7 prohibits automated access EXCEPT "where Anthropic otherwise explicitly
  permits it." The official `claude` CLI is the explicitly permitted surface.
- Anthropic's own documentation shows scripted examples: `tail -f app.log | claude -p "..."`;
  GitHub Actions on cron; fully automated CI/CD pipelines with zero human interaction are cited
  as permitted use.
- Multiple secondary sources confirm: "Running the genuine claude subprocess on any infrastructure
  = allowed."
- No explicit Anthropic statement prohibits always-on, multi-session PTY-driven automation of
  the official interactive CLI.

The structural ambiguity (new as of June 15, 2026):
- The `-p` (headless/print) mode now draws from the Agent SDK credit pool, NOT the general
  subscription. This is metered. Source: groundy.com confirms "`claude -p` subprocess invocations
  confirmed as permitted but draw from the new Agent SDK credit pool rather than the general
  subscription limit starting June 15, 2026."
- The PTY-drive-interactive approach (non-`-p` interactive mode) has not been explicitly
  addressed in the June 15 reclassification. It presumably continues to draw from subscription
  limits.
- The key question for always-on / unattended use: if interactive-mode usage at scale is metered
  in the future (or triggers rate-limiting as non-"ordinary individual" use), this approach may
  encounter throttling — not explicit prohibition, but practical friction.

Summary: No prohibition found. Grey in the sense that: (a) no Anthropic statement covers
unattended/always-on interactive CLI orchestration explicitly, and (b) the June 15 reclassification
of `-p` shows Anthropic is actively drawing architectural lines between subscription and
programmatic use. The interactive PTY path sits in the space between those two lines — currently
unaddressed.

SOURCE:
https://autonomee.ai/blog/claude-code-terms-of-service-explained/ (M)
https://kersai.com/anthropic-killed-third-party-claude-access-heres-every-workaround-that-still-works/ (M)
https://groundy.com/articles/anthropic-bans-third-party-use-subscription-auth-three-stage-repricing/ (M)
https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html (M)

CONFIDENCE: M — no official Anthropic statement addressing PTY/interactive-mode unattended
orchestration specifically. Inference from surrounding policy landscape.

IMPACT: The interposition approach is not prohibited. But the "always-on / unattended" extension
enters genuinely grey territory: not banned, but untested at policy level, and subject to rate
limits calibrated against "ordinary individual usage."

ACTION: Flag in the artifact as GREY (policy-untested). Recommend a rate-limit discipline in the
design: back-off, session scheduling, human-interrupt hooks. Do not claim explicit permission for
always-on mode — claim absence of prohibition.

---

### Q1d: Policy changes since June 2026?

WHAT: One confirmed structural change effective June 15, 2026 — the Agent SDK credit pool. This
reclassifies `-p` headless from subscription-draw to metered credit-draw. No policy changes
specific to interactive-CLI automation were found post-June 2026 as of 2026-07-07.

The VentureBeat article (not fetched in full) is titled "Anthropic reinstates OpenClaw and
third-party agent usage on Claude subscriptions — with a catch" — this is the May 2026 partial
reversal; it concerns third-party agents (OpenClaw etc.) drawing from the Agent SDK credit pool,
not the interactive CLI.

No new AUP revision, no new Consumer Terms update, no new Claude Code-specific policy statement
found after June 15, 2026.

SOURCE:
https://groundy.com/articles/anthropic-bans-third-party-use-subscription-auth-three-stage-repricing/ (M)
https://www.infoworld.com/article/4171274/anthropic-puts-claude-agents-on-a-meter-across-its-subscriptions.html (M)
https://venturebeat.com/technology/anthropic-reinstates-openclaw-and-third-party-agent-usage-on-claude-subscriptions-with-a-catch/ (M)

CONFIDENCE: M — search coverage good; a July-specific policy change could exist and not yet be
indexed.

IMPACT: The June 15 credit-pool split is the most important recent change. It does NOT directly
affect the interactive PTY approach, but it signals Anthropic's intent to meter programmatic use.

ACTION: Monitor. If Anthropic extends credit-pool metering to interactive-mode sessions, the cost
model of always-on orchestration changes significantly.

---

## Findings — Prior Art (Q2)

Four closest projects as of 2026-07-07:

### 1. claude-session-driver (github.com/obra/claude-session-driver)
One-line: tmux-based multi-session Claude Code orchestrator using hook-event JSONL streams for
turn completion, not raw PTY parsing — v2.0.1, May 17 2026, actively maintained (153 commits).
Status: ACTIVE. Uses Claude Code's own hooks system (structured events) rather than screen-scraping.
Works with official CLI; subscription OAuth compatible (no API key required by design).

### 2. tmuxlet (in bradAGI/awesome-cli-coding-agents)
One-line: Rust single-binary that wraps interactive coding CLIs (Claude Code, Codex, Gemini CLI,
opencode, pi, Cursor) inside tmux and exposes a normalized blocking interface — explicitly targets
subscription bucket, not Agent SDK credits.
Status: ACTIVE. Closest prior art to the interposition core: PTY-drive + blocking-call
normalization. Completion detection mechanism not fully documented in public sources.

### 3. primeline-ai/claude-tmux-orchestration (github.com/primeline-ai/claude-tmux-orchestration)
One-line: Multi-worker Claude Code orchestration with heartbeat monitoring and file-based
coordination — parallel-worker harness rather than single-session PTY interposition.
Status: ACTIVE (listed, detail depth not confirmed).

### 4. Claude Squad (vibecodinghub.org/tools/claude-squad)
One-line: Terminal-native orchestration for managing multiple Claude Code agents across isolated
git workspaces — supervisor/pause/review UI, not a headless PTY harness.
Status: ACTIVE, 2026. Higher-level UX layer; not the low-level completion-detection primitive.

Note: rusty-art/claude-tmux exists but focuses on persistent sessions and context preservation for
subagents, not on completion detection or programmatic driving. Low activity (25 commits, 0 stars).

SOURCE:
https://github.com/obra/claude-session-driver (fetched 2026-07-07)
https://github.com/bradAGI/awesome-cli-coding-agents (fetched 2026-07-07)
https://github.com/primeline-ai/claude-tmux-orchestration (search result 2026-07-07)
https://vibecodinghub.org/tools/claude-squad (search result 2026-07-07)

CONFIDENCE: H for claude-session-driver (fetched directly); M for tmuxlet (no direct repo fetch);
M for others (search result depth only).

IMPACT: Prior art is real and active. The interposition approach is not wheel-reinvention if it
targets a distinct capability: specifically, completion detection without relying on Claude Code's
hooks system (which requires the hooks to be installed and running) or without `-p` (which now
draws from credit pool). The niche: subscription-native, hook-free, PTY-pure completion detection
for unattended/multi-project orchestration.

---

## Findings — ACP (Q3)

WHAT: ACP (Agent Client Protocol, Zed) as of 2026-07-07 is a real, active open standard (Apache
license) with Claude Code now in public beta via ACP in Zed. The protocol is JSON-RPC over stdio
for local agents; HTTP/WebSocket for remote (remote support is "work in progress").

Critically for the interposition study: Claude Code in Zed runs via an adapter that wraps the
Claude Code SDK — NOT the interactive CLI binary. The Xuanwo/acp-claude-code bridge (the original
independent adapter) is deprecated and archived (last release v0.8.0, September 2025). The active
implementation is @zed-industries/claude-code-acp, maintained by Zed.

Completion signal: ACP uses JSON-RPC structured replies with streaming responses converted to ACP
format. Structured turn-end events are implied by the protocol (JSON-RPC is inherently
request/response shaped), but the exact turn-completion event type/field is not documented in
public-facing docs as of this research run. The protocol spec at agentclientprotocol.com describes
"JSON representations used in MCP where possible" and "custom types for agentic coding UX elements
like diffs."

VERDICT: ACP is NOT a viable clean-parse adapter for the PTY-drive-interactive-CLI approach.
It operates at the SDK layer, not the interactive CLI layer. For the interposition use case — where
the entire point is to drive the interactive product and avoid SDK/API — ACP adds no value and
introduces SDK dependency. ACP would only be relevant if the design were to pivot to SDK-based
orchestration, which contradicts the subscription-native requirement.

If the design later adds an IDE-integration surface (Zed as UI layer over the orchestrator), ACP
is the correct protocol for that bridge. But it is not a completion-signal solution for the PTY
harness itself.

SOURCE:
https://zed.dev/acp (fetched 2026-07-07)
https://zed.dev/blog/claude-code-via-acp (fetched 2026-07-07)
https://zed.dev/docs/ai/external-agents (fetched 2026-07-07)
https://github.com/Xuanwo/acp-claude-code (fetched 2026-07-07)
https://agentclientprotocol.com (fetched 2026-07-07)

CONFIDENCE: H for "ACP uses SDK not interactive CLI"; M for exact completion-event schema (not
fully documented in public sources).

IMPACT: Ruling out ACP as a clean-parse adapter for the interactive PTY harness. The artifact
should note ACP as a future IDE-integration layer option only.

---

## Summary for Oraculum

### Policy (4 answers)

**Q1a** — "ordinary individual usage": REAL phrase in product docs, NOT in formal terms. Legal
weight = soft (calibrates rate limits, not a prohibition). Do not use as operative clause.

**Q1b** — Bright line on OAuth tokens: CONFIRMED. Token permitted only inside Claude Code /
Claude.ai. PTY-interposition does NOT cross this line — genuine binary, no token extraction.

**Q1c** — Always-on / unattended / multi-session interactive CLI automation: GREY. Not prohibited.
No Anthropic statement covers it. June 15 reclassification of `-p` to credit pool shows Anthropic
is drawing lines; interactive mode sits in the currently-unaddressed space. Rate-limit risk, not
policy risk.

**Q1d** — Post-June 2026 changes: Agent SDK credit pool effective June 15 (metered `-p` and
third-party agents). No further changes found as of 2026-07-07. VOLATILE — monitor monthly.

### Prior art (4 closest)

1. **claude-session-driver** — tmux + hooks/JSONL event streams; ACTIVE May 2026
2. **tmuxlet** — Rust, PTY-wrap + blocking normalization, subscription-native; ACTIVE 2026
3. **primeline-ai/claude-tmux-orchestration** — parallel-worker heartbeat harness; ACTIVE
4. **Claude Squad** — multi-agent workspace supervisor (UX layer); ACTIVE 2026

### ACP verdict

NOT viable as completion-signal adapter for interactive PTY approach. ACP wraps Claude Code SDK,
not the interactive binary. Structural mismatch. Reserve for future IDE-integration surface only.

---

## Sections to refresh

- Anthropic Consumer Terms / AUP (monitor monthly — active policy evolution)
- Agent SDK credit pool mechanics (metering scope may expand to interactive sessions)
- tmuxlet completion-detection mechanism (no direct repo fetch; depth unknown)
- ACP turn-completion event schema (not publicly documented at protocol spec level)
- primeline-ai/claude-tmux-orchestration depth (search result only; repo not fetched directly)
