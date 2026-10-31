# AI Use-Case Memo: Lecture Notes & Self-Check Co-pilot

## 1. Problem Framing & Friction Point
I take the GenAI Basics course (EPAM) alongside full-time work. Every lesson consists of a recorded lecture (~90 min), slides and Markdown guides.
After each lecture I manually rewatch the recording, write a summary, extract key terms and prepare questions for self-review before the homework.
This routine costs 2–3 hours per lesson. Most of it is spent rewinding video and restructuring text, not on understanding; when short on time, I skip notes entirely.

## 2. Technology Classification
The system is a hybrid pipeline:
- File collection, PDF/slide text extraction, folder naming per lesson (`L01/`, `L02/`): deterministic scripts (Software 1.0). An LLM here adds cost and randomness with zero benefit.
- Speech-to-text of the lecture recording: a dedicated ASR model (Software 2.0). It is cheaper and more accurate on audio than a general chat model.
- Review scheduling (when to repeat which topic): a fixed spaced-repetition formula (Software 1.0).
- Structured summary, glossary and self-check questions: Generative AI (Software 3.0 with human review). Foundation models are strong at condensing long text and rephrasing it at different difficulty levels.
An autonomous agent (Software 4.0) is not justified: it is one draft per lesson.

## 3. Data Contracts (Inputs & Outputs)
- Inputs:
  1) Lecture transcript (text from ASR, with timestamps);
  2) Slide text and course guides (Markdown/PDF);
  3) Lesson number and title;
  4) My target language for notes (English or Russian).
- Expected Output: one Markdown file per lesson containing:
  1) Summary of up to 300 words;
  2) Glossary of 10–15 terms with one-line definitions;
  3) 5–10 self-check questions with answers;
  4) Timestamp reference for every key statement, so it can be verified in the recording.

## 4. Blast Radius & Risk Tier
- Risk Tier: 🟡 Yellow Zone (Human-in-the-Loop Co-pilot).
- Potential Failure Modes: the model invents definitions, mixes up terms, or states facts not present in the lecture. Wrong notes lead to wrong understanding and mistakes in graded homework.
- Mitigation Guardrails: the prompt restricts the model to the provided transcript and slides only ("if it is not in the sources, write *not covered*"); low temperature; mandatory timestamps for every claim.

## 5. Human-in-the-Loop Control Gate
1. The draft is saved as `notes-draft.md` and is never treated as final.
2. I check every glossary entry and answer against its timestamp in the recording or the slide.
3. I correct or delete wrong lines and rename the file to `notes.md` — only this reviewed version is used for studying.
Self-check questions are answered by me first, before I look at the generated answers.

## 6. Architectural Taboo (What Will NEVER Be Automated)
The language model is strictly prohibited from:
1. Writing, committing or pushing homework to the `genai-homeworks` repository or submitting it in the course portal.
2. Answering graded course tests or assignments on my behalf.
3. Sending lecture materials or my personal data to third-party services outside the approved tool.
Homework authorship and submission always remain a manual, human action.
