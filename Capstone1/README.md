# Capstone 1 — Voice Brief → Image
**Student:** Kodirjon Khayitov  `kodirjon_khayitov@student.itpu.uz` 
**Notebook (Colab, view access):** https://colab.research.google.com/drive/1i79aAi9-ogzYyu5EqeO1uAX6q4z2nfwl
**Slides:** https://claude.ai/artifact/P7cSxyvPecBf1ChvBbxSVQ

## Pipeline

my voice (25 s) → Whisper small (speech to text) → Gemini 2.5 Flash (text to image prompt) → SD-Turbo (image)

## Brief

> I need a banner image for a delivery app. The most important thing is one courier in an orange jacket riding a red bicycle across an empty city street. Early morning, warm sunrise light. The style is a cozy watercolor illustration. On his back there is one navy blue backpack, and at the top a short caption: Fast and Friendly.

Style: watercolor · Format: landscape 16:9 · Edit: "Change only the bicycle colour to blue, keep everything else the same." · Bonus: B (series of three scenes).

## Key findings

| Stage | What went wrong | What I did |
|---|---|---|
| Whisper | First take (53 s) was garbled; second take (25 s): "All is back" instead of "On his back", caption in lowercase | Re-recorded, fixed the rest in `corrected_transcript` |
| Gemini | Lost "banner for a delivery app", "one" and "on his back"; added "inviting mood" | Compared the prompt with my requirement list |
| SD-Turbo | Backpack orange instead of navy, bicycle dark red, no caption | Checked colours, count and text on the image |
| Edit | The box and trousers turned blue, the bicycle did not | Before / after comparison |

## Files

- `Capstone1_Khayitov_Kodirjon.ipynb`: the notebook with all outputs (download from Colab: File → Download → Download .ipynb).
