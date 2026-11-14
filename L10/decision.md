# L10 • Decision card

**Team task:** first-pass triage of syslog events from our internal network (switches and routers): give each event a category (link up/down, authentication failure, configuration change, hardware/environment, other) and a one-line explanation for the duty engineer.

| Question (slide 27) | Answer |
|---|---|
| **Data boundary** | **Internal-only.** Logs contain internal hostnames, IP addressing, interface names, user names of administrators and configuration fragments. They must not go to an external API or to rented external infrastructure. |
| Approved on external infrastructure (Runpod)? | No |
| Approved at a model-provider API (Gemini, ChatGPT)? | No |
| **Volume** | ≈ **100 events per day** (*assumption*; the real count will be measured during the pilot), arriving in bursts after incidents |
| **Latency need** | Not real-time: a batch every 15–30 min is acceptable, because a person reviews the results |
| Measured local speed | ≈ 56 tok/s, ≈ 12 s per short task with Think ON → 100 events ≈ 20 min of GPU time per day; less with Think OFF (not measured) |
| **Cost per accepted task** | Local ≈ **$0.00004** (electricity estimate, hardware already owned); cloud API ≈ $0.00065 (HW03 measurement), but the API is **not allowed** for this data |

## Decision: **workstation / internal server** (local open model)

The logs are internal-only, so a cloud API and an external Runpod Pod or Serverless deployment are ruled out by the data boundary before price or speed even matter. The test showed that Granite 4.2 8B Q4_K_M fits completely in an 8 GB laptop GPU (5.6 GB used). It produced correct structured JSON for classification with 0 retries, and about 100 events a day is only ~20 minutes of GPU time. The local model makes mistakes: it read a field name too literally in task 3. So its output is only a **first-pass suggestion**, and the duty engineer confirms every category. Next step: a pilot on 30–50 *anonymised or synthetic* log lines with fixed checks and a measured acceptance rate. If it holds up, move from the laptop to an always-on internal server with the API on `localhost` only, or behind authentication inside the internal network.
