"""My first MCP server: a read-only directory of sessions from the adjacent sessions.json."""
import json
from pathlib import Path

from mcp.server import MCPServer

# The data file always sits next to this script, whatever folder the terminal is in.
SESSIONS_FILE = Path(__file__).resolve().parent / "sessions.json"

mcp = MCPServer("my-session-directory")


@mcp.tool()
def get_session(session_id: str) -> dict:
    """Look up one session by its ID (for example W101) in the local sessions.json.

    Returns {"found": true, "session": {...}} when the ID exists,
    otherwise {"found": false, "session_id": ..., "message": "Session not found"}.
    """
    # Read the file on EVERY call, so an edit to sessions.json is visible immediately.
    data = json.loads(SESSIONS_FILE.read_text(encoding="utf-8-sig"))
    for record in data.get("sessions", []):
        if record.get("id") == session_id:
            return {"found": True, "session": record}
    return {"found": False, "session_id": session_id, "message": "Session not found"}


if __name__ == "__main__":
    # stdout is reserved for MCP messages, so the server never prints anything.
    mcp.run(transport="stdio")
