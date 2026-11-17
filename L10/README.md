# L10 • Running an open model locally and comparing it with the cloud

**Author:** Kodirjon Khayitov 
**Reviewer:** `ihar_rubanovich@epam.com` 
· **Date:** 2026-11-15 · **Option:** A (LM Studio, no command line)

## Computer
| | |
|---|---|
| GPU | NVIDIA GeForce RTX 5060 Laptop, **8.0 GB dedicated** (0.0 GB used at idle; the screen runs on the AMD Radeon 610M iGPU) |
| RAM | 32 GB DDR5-5200 (31.3 GB usable), 16.5 GB free at idle |
| CPU | AMD Ryzen 7 8745HX, 8 cores / 16 threads |
| Disk | NVMe SSD, 298 GB free on C: |

## Model
| | |
|---|---|
| Model | **IBM Granite 4.2 8B**, dense 8B reasoning model (`<think>` on by default) |
| Publisher / repo | **ibm-granite/granite-4.2-8b-GGUF**, official IBM repository on Hugging Face (≈ 282 k downloads). A `lmstudio-community` copy also exists; I took the official one. |
| Format | **GGUF, Q4_K_M**, file **5.35 GB** (BF16 original ≈ 17.6 GB would not fit) |
| Licence | **Apache 2.0**, commercial use allowed (model card) |
| Native context | 128K (131 072 tokens); **loaded with 4 096** |
| App | LM Studio (classic, not Bionic), GPU offload 40/40 layers, Think ON |

## Memory: estimate vs measurement
- **Preliminary estimate:** file 5.35 GB × 1.25 ≈ **6.7 GB**. That leaves about 1.3 GB of the 8 GB VRAM for the OS, so the context stays short.
- **Measured after loading** (Task Manager, ctx 4096): **5.6 / 8.0 GB dedicated VRAM**, shared GPU memory 0.1 GB, so the model sits **fully on the GPU**. System RAM rose from 14.8 to 21.8 GB (LM Studio app, runtime and the mapped model file).
- **Caveat:** the ×1.25 rule only holds for a short context. The KV cache grows with the context length and during generation. With 32K or more of context it would not fit in 8 GB: layers or cache would spill into shared RAM and the speed would drop sharply. The runtime (LM Studio) also needs its own RAM. So I measured at the target context of 4096 instead of trusting the formula.

## Speed
About **56 tok/s** on all three tasks (55.94 / 56.20 / 56.00). Time to first token was 0.16–1.76 s, and a full answer took about 11–13 s. Most of the 500–740 generated tokens are hidden "thinking"; the visible answer is 20–60 tokens. See `speed.png`.

## Conclusion
Both models passed all 3 tasks on the first attempt (6/6 runs, 0 retries). The cloud (Gemini, "Авто" mode) was about 4× faster (2–3 s vs 11–13 s) and wrote slightly better text. However, it **added facts** to the customer reply (a "carrier" and "tracking details" that do not exist in the source). The local model misread one field name ("its source is in transit"). For synthetic or public text the cloud is the faster choice. For data that must not leave the organisation, an 8B model on an 8 GB laptop GPU is good enough for short classification and summary work if a human checks the output. Details are in `results.md`; the choice for a real team task is in `decision.md`.

## Security
- Only the **synthetic** prompts from `tasks.md` were used (DEMO-17, W101, fictional units), with no real customers or logs.
- The model was used in the LM Studio chat. Server settings: **Serve on Local Network = OFF**, CORS OFF, port 1234, so nothing is reachable from other devices (`img/server_settings.png`). If the network option is ever turned on, *Require Authentication* must be turned on too.
- The model comes from a **known publisher**: the official `ibm-granite` organisation, Apache 2.0. Fine-tunes from unknown authors (e.g. "decensored" variants in the search results) were not used.
- Screenshots contain no names, e-mails, SSID or IP addresses.

## Files
`results.md` · `speed.png` · `decision.md` · `img/` (raw screenshots: answers, stats, memory, server settings)
