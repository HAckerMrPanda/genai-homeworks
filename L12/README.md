# L12 • Local MCP server

I used Claude (Anthropic) as the AI assistant to create a local MCP server for `sessions.json`; it wrote `server.py` from AI_PROMPT_EN.txt, and I did not copy the reference server. The client is the supplied `check.py`, which starts my `server.py` as a separate local process and talks to it through MCP over stdio, so no website or browser is involved. The server exposes exactly one tool, `get_session(session_id)`, and on every call it reads only the adjacent `sessions.json` (read-only, path taken from `__file__`). In the first run W101 returned `found=true` with start 18:30, and W999 returned `found=false` with "Session not found" and no invented facts. Then I changed only `"start"` of W101 to 20:00 in `sessions.json`, did not touch the server code, ran the same check again and received start 20:00, while W999 stayed `found=false`. The two reports in `results/` show that the only difference in the source snapshot is the start time, and the check confirmed both times that the server did not modify the file. The tool was chosen by the client code, not by a model: AI helped write the server, but no model was used during the calls (`"model_used": false`).

| Run | Report in `results/` | W101 start | W999 | Server modified the file |
|---|---|---|---|---|
| 1, before editing | `check-20261115T040144580839Z.json` | 18:30 | found=false | No |
| 2, after editing | `check-20261115T040749829947Z.json` | 20:00 | found=false | No |

Screenshots of both runs on my Windows laptop: `img/run1_18-30.png`, `img/run2_20-00.png`.
