---
name: l13-support-triage
description: One-batch semantic triage for the bounded L13 native-agent protocol.
---
# One-batch semantic triage

Read only runtime/packets/triage.json, once. It contains source IDs/text, actual policy and contract. Write the complete classifications JSON once; run `python scripts/stage_tool.py triage-check` once, blocking. Do not reread business-policy/routing/source files or inspect the output after a valid receipt. Review is a separate role. On failed validation return the error and stop; no repeated repair loop.
