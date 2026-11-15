# L13 • A support team of four agents

**Author:** Kodirjon Khayitov · **Date:** 2026-11-15
**Tool:** Antigravity (Local), model Gemini 3.8 Flash High, Windows 11
**Input:** the prepared teaching input from `scripts/classroom.py prepare --lang en`. These are 5 synthetic classroom requests (`classroom:1`–`classroom:5`, source `classroom-synthetic`). My own Telegram channel was **not** connected. No messages were sent and no network collection was done.

## What is submitted
| Path | What it is |
|---|---|
| `.agents/agents/l13-collector.md`, `l13-triage.md`, `l13-reviewer.md`, `l13-coordinator.md` | the four role files, as assembled in the teaching copy |
| `.agents/skills/l13-support-triage/SKILL.md` | the triage skill |
| `runtime/telegram_report.html` | **the operator queue** (open in a browser) |
| `runtime/inbox.json` | the 5 source requests |
| `runtime/classifications_initial.json` | triage decisions before review |
| `runtime/review.json` | reviewer decision on the flagged case |
| `runtime/support_children.json`, `runtime/agent-run.json` | actual conversation IDs of the three child agents; run status `completed`, 0 Telegram sends |
| `runtime/classifications_final.json`, `runtime/review_binding.json` | final decisions (identical to initial: 0 amendments); flagged = reviewed = `classroom:5`, `initial_preserved: true`, `customer_actions_executed: 0` |
| `runtime/intake.json`, `runtime/run_plan.json` | frozen-replay intake: 5 messages, `network_requests: 0`, `outgoing_messages_sent: 0`; input/policy hashes |
| `img/` | screenshots: assembly + prepare, the first failed run, the successful run |

The policy `.agents/rules/support-policy.md` was **not changed**, so it is not included.

## The four roles (what each does)
- **l13-collector** (flash): runs `stage_tool.py collect` once. It imports the frozen teaching input (no Telegram calls, no sends) and prepares the triage packet.
- **l13-triage** (flash): reads the packet once and gives every request a category, priority, reason and `review_required`. It writes `classifications.json` and runs `triage-check`.
- **l13-reviewer** (pro): re-checks **only** the automatically flagged requests. It accepts or amends each one with a reason, then runs `review-check`, which keeps the initial decisions and renders the HTML.
- **l13-coordinator** (inherits the chat model): reads `EXECUTION_PLAN.md`, calls the three roles in order, records their IDs and runs `finish-support`.

Code, not a model, validates the JSON, assigns the queue (`billing→Billing`, `access→Support`, `bug→Engineering`, `feature→Product`, `other` or review → Manual review) and renders the HTML.

## How it was run
1. Assembly in Antigravity chat (screenshot `img/01_…`). The agent confirmed that the policy, skill and four roles already contained the complete templates, so it kept them unchanged without editing scripts. It then ran `python scripts/classroom.py prepare --lang en`, which bound the policy to the 5 classroom requests.
2. My Antigravity version has **no agent selector** in the chat (the dropdowns contain only models and permission modes; `@` only offers Rules/Conversation/Drive). I therefore started a new conversation in the project and gave the coordinator role explicitly:
   ```
   Act as l13-coordinator: follow .agents/agents/l13-coordinator.md exactly. Execute the support phase of EXECUTION_PLAN.md. Use the configured request source and invoke the named subagents l13-collector, l13-triage and l13-reviewer in order. Assess all supplied requests, review flagged cases and prepare the queue. Summarize the responsible teams and where to open the HTML report. Stop after support.
   ```
3. **First attempt failed** (`img/00_…`). The collector subagent started, but `python.exe failed to run: The file cannot be accessed by the system`. Following the contract, the agents stopped and did not retry. Cause: `python` resolved to a Python Install Manager / Microsoft Store alias in my user profile, which the agents' command sandbox cannot execute. **Fix (infrastructure only, no project files changed):** I installed Python 3.13 for all users into `C:\Program Files\Python313`, so it is first on PATH, then rebooted.
4. **Second attempt succeeded** (`img/02_…`). The three named subagents ran as real child conversations:
   - l13-collector `507774c5-0945-4327-9c3c-7e6af8e90e3f`: 5 messages, 0 Telegram sends, 0 network requests
   - l13-triage `527680c2-86ee-4bcb-9c44-d6cf0d61009f`: 5 classified, 1 flagged
   - l13-reviewer `d13a451d-880f-48df-898a-add9a155fb34`: 1 reviewed, 0 amended
   - `finish-support` completed; report at `runtime/telegram_report.html`

## The queue (runtime/telegram_report.html)
5 messages · 4 queues · 1 manual review.

| ID | Request | Category / priority | Queue |
|---|---|---|---|
| classroom:1 | My card was charged twice ($49.99 x 2) for order 9401. | billing / **high** | Billing |
| classroom:2 | I cannot sign in. The login form keeps reloading. | access / normal | Support |
| classroom:3 | I received a sign-in code I did not request. Someone may be accessing my account. | access / **high** | Support |
| classroom:4 | Opening any active order crashes the app for our entire shift of 15 employees. | bug / **high** | Engineering |
| classroom:5 | Everything broke again. Please help! | other / normal, review | **Manual review** |

### A clear request: classroom:1
| Field | Value |
|---|---|
| Source text | "My card was charged twice ($49.99 x 2) for order 9401." |
| Team / priority | Billing / high |
| Rationale (agent) | "Customer reported duplicate charges for order 9401." |
| Why it is correct | The policy sets `high` for "duplicate charging for the same order", and payments belong to billing. The message names one order, the amount and that it was charged twice, so nothing is missing. It was not flagged, which is correct. |

### An unclear request: classroom:5
| Field | Value |
|---|---|
| Source text | "Everything broke again. Please help!" |
| Team / priority | other / normal, `review_required=true` → Manual review |
| Rationale (triage) | "Insufficient details provided to determine the issue." |
| Reviewer | **accepted** the initial decision: "the message provides insufficient details to identify a specific feature or widespread blockage". No amendment, so the uncertainty was not replaced by a guess. |
| What the operator must clarify with the customer | **What** exactly stopped working (which screen or feature: orders, payment, sign-in?); **what happens** (error message, crash, blank screen); **which order or account**; **when** it started and whether "again" means the same problem as an earlier ticket (number?); **how many people** are affected, to decide whether it is a widespread blockage that would justify `high`. Manual review sends nothing to the customer automatically; the operator asks these questions. |

## Queue check
| Question | Result |
|---|---|
| No request was lost | ✅ 5 input IDs → 5 rows in the report, same IDs and original text (`classroom:1`–`classroom:5`). |
| Teams and urgency make sense | ✅ Duplicate charge → Billing/high. Ordinary sign-in failure → Support/normal. An unrequested sign-in code is *suspected unauthorized access*, so it is high under the policy. Crash for a whole shift of 15 people is a *widespread work blockage* → Engineering/high. |
| Uncertainty stays visible | ✅ "Everything broke again" goes to Manual review with a "Human review" badge. Triage flagged it and the reviewer kept the flag instead of inventing a diagnosis. |

**Observations**
- The coordinator's chat summary describes the queues in generic terms ("Billing & Finance Operations" etc.). Those team descriptions are not in the policy. The authoritative result is the HTML queue, which is computed by code.
- The provenance line in the HTML is in Russian (a fixed string in the prepared tool), although the run was `--lang en`.

## Security
Synthetic data only. Frozen replay: 0 Telegram sends and 0 network requests. No tokens, `demo_v3/.env` or `.local/` are submitted. No customer actions were performed: no refunds, no replies.
