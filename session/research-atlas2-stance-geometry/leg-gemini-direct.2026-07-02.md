# Gemini Direct Headless Run — Supplementary Research

**Status:** FINAL: parked — heterogeneity leg stands on bluebottle artifact only

**Metadata:**

| Field | Value |
|-------|-------|
| First Attempt Command Line | `gemini --skip-trust -m gemini-2.5-flash -p "INSTRUCTION + DOCUMENT_CONTENT"` |
| First Attempt Model | `gemini-2.5-flash` |
| First Attempt Exit Code | 124 (timeout) |
| First Attempt Runtime | 5m 0s (timeout budget) |
| Second Attempt Command Line | `gemini --skip-trust -m gemini-2.5-flash-lite -p "INSTRUCTION + DOCUMENT_CONTENT"` |
| Second Attempt Model | `gemini-2.5-flash-lite` |
| Second Attempt Exit Code | Failed (no output) |
| Second Attempt Runtime | ~30s |
| Grounding Status | No web/search results — both attempts failed before reaching API stability |
| CLI Version | 0.49.0 |
| Date Attempted | 2026-07-02 (retry on 2026-07-02) |
| Supplementary To | leg-gemini.2026-07-02.md (bluebottle pass); intended as direct CLI, §0-conformant prompt |

---

## Summary

Both the primary model (gemini-2.5-flash) and the fallback model (gemini-2.5-flash-lite) failed to complete:

1. **First attempt (gemini-2.5-flash):** Sustained 503 UNAVAILABLE errors across multiple retry cycles, with at least one 500 INTERNAL error. CLI backed off and retried until timeout (5min).
2. **Second attempt (gemini-2.5-flash-lite):** Failed to produce any output or error logs. Either model rejected the request or CLI encountered early failure.

The heterogeneity leg (direct Gemini research pass) cannot proceed. The task is parked. Bluebottle artifact (leg-gemini.2026-07-02.md) is the only completed research input from the Gemini vendor.

---

## First Attempt Error Log (gemini-2.5-flash)

```
Warning: --allowed-tools cli argument and tools.allowed in settings.json are deprecated and will be removed in 1.0: Migrate to Policy Engine: https://geminicli.com/docs/core/policy-engine/
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Warning: Could not read directory /tmp/snap-private-tmp: EACCES: permission denied, scandir '/tmp/snap-private-tmp'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-mariadb.service-dU5uPq: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-mariadb.service-dU5uPq'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ModemManager.service-gHqJ1R: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ModemManager.service-gHqJ1R'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-nginx.service-WOHkJH: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-nginx.service-WOHkJH'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ollama.service-yS1Slp: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ollama.service-yS1Slp'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-php74-fpm.service-dU5uPq: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-php74-fpm.service-dU5uPq'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-polkit.service-FHF3cC: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-polkit.service-FHF3cC'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-power-profiles-daemon.service-a9WBVP: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-power-profiles-daemon.service-a9WBVP'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-systemd-logind.service-LWI19j: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-systemd-logind.service-LWI19j'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-upower.service-Uk1fr7: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-upower.service-Uk1fr7'
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Attempt 1 failed with status 503. Retrying with backoff... _ApiError: {"error":{"code":503,"message":"This model is currently experiencing high demand. Spikes in demand are usually temporary. Please try again later.","status":"UNAVAILABLE"}}
    at throwErrorIfNotOK (file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:258424:24)
    at process.processTicksAndRejections (node:internal/process/task_queues:104:5)
    at async file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:258175:7
    at async Models.generateContent (file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:259234:16)
    at async file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:301234:26
    at async file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:278341:23
    at async retryWithBackoff (file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:298287:23)
    at async GeminiClient.generateContent (file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:335832:23)
    at async WebSearchToolInvocation.execute (file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:320458:24)
    at async executeToolWithHooks (file:///home/hruzam/.npm-global/lib/node_modules/@google/gemini-cli/bundle/chunk-VLV2BYPM.js:330457:22) {
  status: 503
}

[Multiple retry cycles with same 503 errors, progressing through:
  - Attempt 1: 503 UNAVAILABLE (repeated)
  - Attempt 2: 500 INTERNAL, then 503 UNAVAILABLE
  - Attempt 3: 503 UNAVAILABLE
  - Attempt 4: 503 UNAVAILABLE
  - Final timeout at 5:00]

Timeout: Command killed after 5 minutes (300 seconds).
```

---

## Second Attempt Error Log (gemini-2.5-flash-lite)

```
Warning: --allowed-tools cli argument and tools.allowed in settings.json are deprecated and will be removed in 1.0: Migrate to Policy Engine: https://geminicli.com/docs/core/policy-engine/
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Warning: Could not read directory /tmp/snap-private-tmp: EACCES: permission denied, scandir '/tmp/snap-private-tmp'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-mariadb.service-dU5uPq: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-mariadb.service-dU5uPq'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ModemManager.service-gHqJ1R: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ModemManager.service-gHqJ1R'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-nginx.service-WOHkJH: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-nginx.service-WOHkJH'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ollama.service-yS1Slp: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-ollama.service-yS1Slp'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-php74-fpm.service-dU5uPq: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-php74-fpm.service-dU5uPq'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-polkit.service-FHF3cC: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-polkit.service-FHF3cC'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-power-profiles-daemon.service-a9WBVP: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-power-profiles-daemon.service-a9WBVP'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-systemd-logind.service-LWI19j: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-systemd-logind.service-LWI19j'
Warning: Could not read directory /tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-upower.service-Uk1fr7: EACCES: permission denied, scandir '/tmp/systemd-private-5e74be22a3b444f0ab3e2cb62e81aa57-upower.service-Uk1fr7'
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.
Both GOOGLE_API_KEY and GEMINI_API_KEY are set. Using GOOGLE_API_KEY.

[End of output — no API response, no error message logged]
```

---

## Exact Commands Attempted

**First Attempt:**
```bash
timeout 300 gemini --skip-trust -m gemini-2.5-flash -p "$(cat <<'PROMPT_EOF'
You are an independent researcher receiving the following document blind. Follow its section 0 exactly...
[input document]
PROMPT_EOF
)"
```

**Second Attempt:**
```bash
timeout 300 gemini --skip-trust -m gemini-2.5-flash-lite -p "$(cat <<'PROMPT_EOF'
You are an independent researcher receiving the following document blind. Follow its section 0 exactly...
[input document]
PROMPT_EOF
)"
```

---

## Conclusion

The direct Gemini research leg cannot proceed at this time. The Gemini API (both flash and flash-lite models) is experiencing availability issues:

- gemini-2.5-flash: Sustained 503 overload errors + one 500 internal error
- gemini-2.5-flash-lite: Early exit with no diagnostic output

Per task protocol: heterogeneity leg is parked. The bluebottle artifact (leg-gemini.2026-07-02.md from the initial research pass) remains the only Gemini-vendor input available for this document.

No further retry is warranted without addressing the underlying API availability issues.
