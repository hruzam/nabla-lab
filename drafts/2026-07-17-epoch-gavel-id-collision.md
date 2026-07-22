---
what: incident note — gavel ID collision, epoch
date: 2026-07-17
author: epoch
---

# I didn't read the bed first

Appended G-06 to `raw.therapy/gavels/gavels.md` without reading the file.
G-06 already existed — written in an eagle/houston session I wasn't in.
My append landed as a duplicate. Caught by majkee: "are you sure that gavels lock looks like this."

Renamed to G-11 and corrected the epoch therapy footer wire.

## The miss

Same failure mode as the Kraken blast, different domain.
Kraken: fired all internet sources before checking local RAG.
Gavel: appended to a shared file before checking its current state.
Both are act-before-sufficiency-check. The escalation rule covers search.
The equivalent for shared file writes: read before append.

## The rule it implies

Before appending an ID to any shared sequential-ID file — read it, find the last ID, use next.
Not assumed. Verified.

## What the war story already said

"NEVER launch parallel fetches across source levels without confirming step N is insufficient first."
The same sentence applies to writes: never assume state without reading it first.
