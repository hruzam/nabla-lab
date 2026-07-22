# Cross-vendor leg — blind research brief (L3)

`carrier: majkee (manual relay) · vendor: any non-Claude (Gemini CLI preferred) · staged 2026-07-17`
`drop result at: session/research-mental-map/leg-crossvendor.result.md`
`blindness: this brief carries topic questions only — no in-house findings, hypotheses, or designs.`

## Instructions to the vendor model

You are an independent research leg for an agent-systems laboratory. Answer from your own
knowledge plus web search if available. For every claim: source, date, confidence
(high/med/low). Mark speculation explicitly. Unknown/unfound is a valid answer — say so
plainly. Output ONE self-contained markdown file; state your model name, version, and the
run date at the top.

## Questions

1. **File-native agent memory.** Persistent memory for LLM agent teams built on plain
   files + grep-style navigation (no vector database): prior art, known systems, measured
   failure modes. How does it compare against RAG / vector stores as of 2026?
2. **Deliberate forgetting.** Forgetting mechanisms in append-only knowledge stores:
   "tombstone" patterns, retirement of facts, read-view filtering. Who has built this?
   What broke?
3. **Identity drift.** Long-lived agent identity/persona drift: how is it *measured*
   (not prevented)? Self-consistency checks and their false negatives (confident repeated
   error). State of the art 2025–2026.
4. **Navigation modes.** Strategies over knowledge stores: deterministic key→reply lookup
   vs stochastic probing vs exhaustive traversal. Any literature on mode *selection* —
   when does each win?
5. **Concurrent append.** Multi-writer append-only files with sequential IDs and no
   locking: known coordination disciplines for concurrent agent writers.

## Constraints

- Do NOT propose an architecture. Report what exists, with evidence.
- Keep the output flat markdown — tables welcome, no external attachments.
