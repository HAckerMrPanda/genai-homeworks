"""Real MCP stdio client. Calls the student server; never imports its functions."""
import argparse
import asyncio
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import sys

from mcp import Client, StdioServerParameters

HERE = Path(__file__).resolve().parent


def error_text(error):
    if isinstance(error, BaseExceptionGroup):
        return "; ".join(error_text(child) for child in error.exceptions)
    return str(error)


async def check():
    parser = argparse.ArgumentParser()
    parser.add_argument("--lang", choices=["ru", "en"], default="ru")
    args = parser.parse_args()
    t = lambda ru, en: ru if args.lang == "ru" else en
    source = HERE / "sessions.json"
    original = source.read_bytes()
    expected = next(r for r in json.loads(original)["sessions"] if r["id"] == "W101")
    server = HERE / "server.py"
    if not server.exists():
        raise RuntimeError(t("Нет server.py. Создайте его с ИИ по AI_PROMPT_RU.txt.",
                             "server.py is missing. Create it with AI using AI_PROMPT_EN.txt."))
    evidence = {"time_utc": datetime.now(timezone.utc).isoformat(), "transport": "stdio",
                "server_sha256": hashlib.sha256(server.read_bytes()).hexdigest(),
                "source_sha256": hashlib.sha256(original).hexdigest(),
                "source_snapshot": json.loads(original), "model_used": False, "calls": []}
    connection = StdioServerParameters(command=sys.executable, args=[str(server)], cwd=str(HERE))
    # A working-directory-independent server is required; this also works under a desktop host.
    try:
        async with asyncio.timeout(35):
            async with Client(connection, read_timeout_seconds=15) as client:
                print(t("[OK] MCP-подключение: stdio, локальный процесс", "[OK] MCP connection: stdio, local process"))
                evidence["protocol_version"] = client.protocol_version
                catalog = await client.list_tools()
                names = [tool.name for tool in catalog.tools]
                if names != ["get_session"]:
                    raise RuntimeError(f"Expected exactly get_session; received: {names}")
                print("[OK] tools/list: get_session")
                evidence["tools_list"] = catalog.model_dump(mode="json", by_alias=True)
                for key in ("W101", "W999"):
                    result = await client.call_tool("get_session", {"session_id": key})
                    raw = result.model_dump(mode="json", by_alias=True)
                    if result.is_error:
                        raise RuntimeError(f"MCP tool error for {key}: {raw}")
                    data = raw.get("structuredContent")
                    if data is None:
                        data = json.loads("\n".join(x["text"] for x in raw.get("content", []) if x.get("type") == "text"))
                    evidence["calls"].append({"method": "tools/call", "name": "get_session",
                                              "arguments": {"session_id": key}, "result": data, "raw_result": raw})
                    if key == "W101":
                        if data.get("found") is not True or data.get("session") != expected:
                            raise RuntimeError(t("Ответ W101 отличается от sessions.json. Сервер должен читать файл при каждом вызове.",
                                                 "W101 differs from sessions.json. Read the file on every call."))
                        print(f"[OK] W101: found=true, start={data['session']['start']}")
                        print(json.dumps(data, ensure_ascii=False, indent=2))
                    else:
                        if data.get("found") is not False or data.get("session"):
                            raise RuntimeError("W999 must return found=false without fabricated facts")
                        print("[OK] W999: found=false")
                if source.read_bytes() != original:
                    raise RuntimeError("The server changed sessions.json; only reading is allowed")
                evidence["status"] = "pass"
                print(t("[OK] Ответ совпал с файлом; файл не изменён сервером.",
                        "[OK] Response matches the file; the server did not modify it."))
    except Exception as error:
        evidence["status"] = "fail"
        evidence["error"] = error_text(error)
        raise
    finally:
        directory = HERE / "results"
        directory.mkdir(exist_ok=True)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
        path = directory / f"check-{stamp}.json"
        path.write_text(json.dumps(evidence, ensure_ascii=False, indent=2), encoding="utf-8")
        print(t("Отчёт: ", "Report: ") + str(path))
    print(t("ГОТОВО: локальный сервер ответил через MCP.", "DONE: the local server responded through MCP."))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    try:
        asyncio.run(check())
    except Exception as error:
        print(f"ERROR: {error_text(error)}", file=sys.stderr)
        sys.exit(1)
