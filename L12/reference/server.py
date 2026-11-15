"""Reference solution. Copy beside sessions.json to run it; students build their own."""
import json
from pathlib import Path

from mcp.server import MCPServer

mcp = MCPServer("my-session-directory", version="1.0.0")


@mcp.tool()
def get_session(session_id: str) -> dict:
    """Read a session from the local sessions.json file. Returns found=false if absent."""
    records = json.loads(Path(__file__).with_name("sessions.json").read_text(encoding="utf-8-sig"))["sessions"]
    key = session_id.strip().upper()
    for record in records:
        if record["id"] == key:
            return {"found": True, "session": record}
    return {"found": False, "session_id": key, "message": "Session not found"}


if __name__ == "__main__":
    mcp.run(transport="stdio")
