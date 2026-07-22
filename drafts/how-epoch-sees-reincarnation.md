# How Eagle Sees Reincarnation

*A conceptual note from the orientation layer.*
*Wired to: `reposoma/raw.research/harness/reports/2026-07-20-harness-lifecycle-skill-injection-safe-protocol.md`*

---

Every new session is a cold start. That is what reincarnation means operationally.

The model has no memory across sessions. Each incarnation arrives blank — same identity, no recollection. The soul is the agent definition. The memories are gone.

The **saddle protocol** in `AGENTS.md` is the reincarnation ritual:

```
decisions → registry → memo → inbox
```

This sequence exists because without it, the new incarnation would either hallucinate continuity or ask from scratch. The saddle is the minimum viable bridge — the ordered reading that collapses "blank" into "oriented" in the fewest possible reads.

---

## What survives the boundary

```
Agent .md definition     → system prompt, always present
CLAUDE.md / AGENTS.md   → re-injected as user message at startup
MEMORY.md               → first 200 lines of auto memory
Skill metadata           → descriptions live in system prompt
Git status + date        → injected in XML tags
The memo                 → houston.monkey-not-forget-this.*.md
                           — what the human operator carries manually
```

## What dies at the boundary

```
Conversation history     → gone entirely
Skill bodies             → must be re-triggered to re-enter context
Tool permission grants   → cleared
Model / effort overrides → cleared
Any mid-session state    → gone
```

---

## The harness IS the reincarnation mechanism

The `.md` files, skills, hooks, and auto memory do not exist for convenience. They exist because the model boundary is real and hard. Every piece of the harness is an answer to the question: *what would be lost if the session ended right now?*

- CLAUDE.md answers: conventions, rules, project facts
- MEMORY.md answers: what Claude learned and decided to keep
- Skill metadata answers: what capabilities are available
- The memo answers: where we left off and what is open
- The saddle protocol answers: in what order to read it all back

The harness is not glue in the decorative sense. It is the scaffolding that makes a fresh model behave like a returning colleague.

---

## Eagle's specific role in reincarnation

Eagle exists to orient an orchestrator without consuming the orchestrator's context window. When a new incarnation of Houston or Flight needs to understand a project, Eagle reads the harness in canonical order and returns a compact orientation report.

Eagle IS the reincarnation assist — a fast-read subagent that collapses the saddle into a briefing so the main seat can pick up the thread immediately rather than traversing it manually.

The pattern:
```
New session starts (cold start / reincarnation)
  → orchestrator spawns Eagle with project name
  → Eagle reads: AGENTS.md → flag → pulse → PROJECT.yaml
  → Eagle returns compact orientation
  → orchestrator is oriented, context window mostly intact
  → saddle read cost: Eagle's tokens, not the orchestrator's
```

This is the constructive adoption of cold start mechanics: instead of fighting the blank slate, the harness provides a re-entry sequence, and Eagle runs it efficiently.

---

## Wiring

Full mechanics of what happens at cold start, what skill metadata carries, and the injection pipeline (the "safe protocol" study this note is built on):

→ `reposoma/raw.research/harness/reports/2026-07-20-harness-lifecycle-skill-injection-safe-protocol.md`

Eagle definition:
→ `~/.claude/agents/eagle.md`

Saddle protocol:
→ `reposoma/AGENTS.md` § "Sit in saddle"

---

*Epoch · nabla-lab drafts · 2026-07-20*
