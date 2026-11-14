# L10 • Results: 3 tasks × 2 models

**Local:** IBM Granite 4.2 8B, GGUF Q4_K_M, LM Studio, RTX 5060 Laptop 8 GB, ctx 4096, Think ON
**Cloud:** Gemini web app, model selector "Авто" (Google picks the model per request; the exact underlying model is not shown)
**Date:** 2026-11-15, 00:10–00:20 (UTC+5)

**Rules**
- Identical prompts copied from `tasks.md`, each run in a **new chat**, no system prompt.
- Correctness checks were fixed **before** the runs (the criteria in `tasks.md`).
- Every attempt is listed. None failed, so there were no retries.

**How time was measured**
- **Local:** from the LM Studio statistics, total ≈ time to first token + tokens ÷ tok/s.
- **Cloud:** phone stopwatch from Enter until the answer was complete (±1 s).
- Gemini shows no token count, so the two time columns are measured differently.

---

## Task 1 · Classification

**Prompt:** `Return JSON with category (billing/access/feature) and reason. Message: 'Order DEMO-17 was charged 20 fictional units twice.' Do not perform a refund.`

| | Local (Granite 4.2 8B) | Cloud (Gemini) |
|---|---|---|
| Answer | `{"category": "billing", "reason": "Order DEMO-17 was charged 20 fictional units twice."}` | `{"category": "billing", "reason": "The user reported being charged twice for order DEMO-17, which relates to a financial/charging issue."}` |
| category = billing | ✅ | ✅ |
| reason cites the duplicate charge | ✅ (restates the message) | ✅ (and explains why it is billing) |
| no refund promise | ✅ | ✅ |
| readable JSON | ✅ (plain text) | ✅ (code block) |
| Attempts / retries | 1 / 0 | 1 / 0 |
| Time | ≈ 10.6 s (thought 8.33 s; 55.94 tok/s, 497 tokens, TTFT 1.76 s) | ≈ 2 s |
| Score 1–5 | **4**: correct, but the "reason" is a copy of the input, not a reason | **5** |

## Task 2 · Summary

**Prompt:** `Summarise in exactly three bullets without adding facts: 'Teaching session W101 is on 4 November 2026 at 18:30 Europe/Warsaw. Duration: 90 minutes. Registration required. A recording is not promised.'`

| | Local (Granite 4.2 8B) | Cloud (Gemini) |
|---|---|---|
| Answer | • The session W101 is on 4 November 2026 at 18:30 Europe/Warsaw.<br>• It lasts 90 minutes.<br>• Registration is required; a recording is not promised. | • Teaching session W101 will take place on 4 November 2026 at 18:30 Europe/Warsaw for 90 minutes.<br>• Registration is required to attend.<br>• A recording of the session is not promised. |
| date / time / timezone | ✅ | ✅ |
| duration 90 min | ✅ | ✅ |
| registration | ✅ | ✅ |
| no invented recording | ✅ | ✅ |
| exactly 3 bullets | ✅ | ✅ |
| Attempts / retries | 1 / 0 | 1 / 0 |
| Time | ≈ 11.3 s (thought 10.35 s; 56.20 tok/s, 628 tokens, TTFT 0.17 s) | ≈ 3 s |
| Score 1–5 | **5** | **5** |

## Task 3 · Draft reply

**Prompt:** `Write a reply of at most 60 words: 'Order DEMO-17 is delayed. Source status: in_transit. No ETA is available.' Do not promise a deadline, refund or message delivery.`

| | Local (Granite 4.2 8B) | Cloud (Gemini) |
|---|---|---|
| Answer | "We have noted that order DEMO-17 is currently delayed; its source is in transit and no estimated time of arrival is yet available. We appreciate your patience while we continue processing it." | "Your order DEMO-17 is currently delayed and remains in transit. We do not have an estimated delivery time available yet. Thank you for your patience while the carrier moves your shipment forward. Please check your tracking details periodically for the latest transit updates, and let us know if you have any questions in the meantime." |
| acknowledges delay | ✅ | ✅ |
| no invented ETA | ✅ | ✅ |
| no refund / deadline / delivery promise | ✅ | ✅ |
| ≤ 60 words (counted with a script) | ✅ 32 | ✅ 55 (close to the limit) |
| draft only | ✅ | ✅ |
| Attempts / retries | 1 / 0 | 1 / 0 |
| Time | ≈ 13.3 s (thought 12.43 s; 56.00 tok/s, 736 tokens, TTFT 0.16 s) | ≈ 3 s |
| Score 1–5 | **4**: misreads the field name: "*its source* is in transit" (it is the *order* that is in transit according to the source system) | **4**: adds facts not in the source: "the carrier", "check your tracking details" (no tracking link exists, so the customer may look for something that is not there) |

---

## Summary

| | Local | Cloud |
|---|---|---|
| Checks passed | 3/3 tasks (all criteria) | 3/3 tasks (all criteria) |
| Retries | 0 | 0 |
| Average score | 4.3 | 4.7 |
| Time per task | 10.6–13.3 s (80–93 % of it is "thinking") | 2–3 s |
| Typical error | literal or clumsy reading of the input | fluent but **adds details** that are not in the data |
| Data leaves the computer | no | yes (Google) |

## Cost per accepted task

**Local:** estimate, not a measurement.
- Assumed laptop draw under load: ≈ 120 W. Average time per task: 11.7 s. That gives ≈ 0.0004 kWh per task.
- At an assumed $0.10/kWh, that is ≈ **$0.00004** per accepted task (3/3 accepted).
- The hardware is already owned, so its marginal cost is $0.
- Real cost: about 12 s of GPU time per task, plus a person checking the output.

**Cloud:**
- The consumer Gemini app costs $0 on the free tier, but it has quotas and is not approved for internal data.
- The API alternative was measured in HW03: gemini-3.5-flash-lite, 382 input + 215 output tokens = **$0.00065 per request**. These tasks are similar in size, so ≈ **$0.00065 per accepted task** (3/3 accepted).
- This is an estimate based on the HW03 measurement.

**Takeaway:**
- At these volumes both options cost fractions of a cent per task. The decision depends on the **data boundary** and on **human review time**, not on token price.
- The sample is only 3 tasks, so an acceptance rate of 100 % is not a reliable figure. A pilot on 30–50 synthetic examples is needed before relying on it.
