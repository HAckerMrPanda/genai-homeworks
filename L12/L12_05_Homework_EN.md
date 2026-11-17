# L12 · Homework: your own local MCP server

**Task:** use AI to create a program that reads session facts from a file on your computer. Call it through real MCP and verify the response.

**Result:** test program → MCP → your server.py → sessions.json.

**You need:** Python 3.11+, the AI assistant you used in L11, and internet for the first library installation. Allow 60–90 minutes. AI helps write the code; your job is to run it, verify it and explain the result.

## 1. Prepare the folder

Download **L12_Local_MCP_Homework.zip** from the lesson materials, extract it and open **homework_local**. Work in the extracted folder, not inside the ZIP.

It contains:

- **sessions.json:** synthetic facts for W101;
- **AI_PROMPT_EN.txt:** the complete task for AI;
- **check.py:** a program that actually calls your server through MCP;
- **Run Check EN.cmd:** the Windows launcher;
- **reference/server.py:** a working example to consult if stuck.

Your own **server.py is not yet beside the data**. Create that file. The tester is supplied; do not rewrite it.

Open sessions.json in a text editor. JSON is a text data format: field names are on the left, values on the right. This is a local file on your computer.

~~~json
{
  "sessions": [
    {
      "id": "W101",
      "title": "MCP practice",
      "date": "2026-11-04",
      "start": "18:30",
      "timezone": "Europe/Warsaw",
      "duration_minutes": 90,
      "registration_required": true
    }
  ]
}
~~~

W101 is the session ID; start is its start time; duration_minutes is duration. true means registration is required. There is no W999 record.

## 2. Ask AI to create the server

Open the folder in the AI assistant you used in L11. Send it **the entire AI_PROMPT_EN.txt**. It specifies the library, function, response format and launch method.

The short version is:

> Create server.py beside sessions.json: a local Python MCP server with one tool, get_session(session_id). Read sessions.json on every call and return the matching record. Return found=false if absent. Read-only access. Run through stdio. Do not modify check.py.

For a chat-only assistant, attach sessions.json and requirements.txt with the prompt. Save the generated code as **server.py**, without .txt, beside the data.

Here AI helps **write the program**. The server needs no model to read a file.

## 3. Run it and inspect the first response

On Windows double-click **Run Check EN.cmd**. If Python is missing, install Python 3.11+ from [python.org](https://www.python.org/downloads/) and repeat. First run creates .venv, an isolated Python environment, and installs the MCP library from requirements.txt.

A text window shows check.py starting your server.py as a separate process. MCP uses **stdio**, the process's standard input/output. The tester lists tools and calls get_session for W101 and W999.

You should see:

~~~text
[OK] tools/list: get_session
[OK] W101: found=true, start=18:30
[OK] W999: found=false
DONE: the local server responded through MCP.
~~~

The full W101 response also appears. A JSON report in **results** stores actual requests, responses and a source-file snapshot. Keep the first report. Use Run Check EN.cmd for English output; Run Check.cmd produces Russian output.

The test program starts this local server. It needs no website URL or browser. The connection closes and the server stops after checking. Every run saves a new report.

On macOS/Linux open a terminal in this folder:

~~~bash
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python check.py --lang en
~~~

## 4. Prove the response comes from the file

Change **only** "start": "18:30" to "start": "20:00" in sessions.json and save. AI may help edit the data; do not change server code at this step.

Run the check again. You should now see:

~~~text
[OK] W101: found=true, start=20:00
[OK] W999: found=false
~~~

Keep the second report. Receiving 20:00 after editing demonstrates a working source connection. Leave 20:00 in the final file so the instructor can reproduce your last run.

| Your check | Expected result |
|---|---|
| W101 before editing | Record found, start 18:30 |
| W999 | found=false, no invented session facts |
| Edit the file and call again | Start 20:00 without changing server code |

If you see ERROR or no [OK], send the **exact error** to AI: “Help fix this run. Do not change check.py; explain what failed.” Repeat after fixing it. “It should work” is not a successful call.

## 5. Submit

Place these in **genai-homeworks/L12/**:

1. Your **server.py** and final **sessions.json** with start 20:00.
2. **Two JSON reports** from results: before and after editing. Each includes W101 and W999 calls.
3. **README.md** with 5–8 sentences using the example below. A screenshot is optional.

Do not submit .venv. If you used reference/server.py, say so and still perform both runs yourself.

Example README; adapt it to your actual run:

> I used [AI name] to create a local MCP server for sessions.json. The client is the supplied check.py; the server is my server.py. W101 first returned start 18:30. W999 returned found=false. I edited the file to 20:00, repeated the call and received 20:00. The server reads only one file. Test-client code chose the tool; a model helped write the server but was not used during the call.

## Scoring — 10 points

- 2: the server starts and exposes get_session through MCP;
- 3: W101 is returned and W999 is correctly absent;
- 2: editing the file changes the response to 20:00;
- 2: code, data and two reports are submitted;
- 1: client, server, file and AI roles are explained.

A2A, AWS deployment and external accounts are outside this assignment.

Reviewer: Ihar Rubanovich · ihar_rubanovich@epam.com.
