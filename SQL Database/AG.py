#!/usr/bin/env python3
"""
General-purpose AI agent powered by Claude.

Setup:
    pip install anthropic requests beautifulsoup4
    export ANTHROPIC_API_KEY="your-key"
    python agent.py

Tools: run shell commands, run Python, read/write files, list folders,
fetch web pages, search the web. Risky actions ask for your approval.
"""
import os
import subprocess
import sys
import tempfile

import anthropic
import requests
from bs4 import BeautifulSoup

MODEL = os.environ.get("AGENT_MODEL", "claude-sonnet-5-5")
AUTO_APPROVE = os.environ.get("AGENT_AUTO_APPROVE") == "1"  # set to 1 to skip confirmations
MAX_STEPS = 30
MAX_OUTPUT = 8000  # characters returned to the model per tool call

SYSTEM = (
    "You are a capable autonomous agent. Break tasks into steps, use your tools "
    "to actually do the work, check results, and fix errors. When finished, give "
    "a short summary of what you did and where any files are."
)

client = anthropic.Anthropic()


def clip(text: str) -> str:
    return text if len(text) <= MAX_OUTPUT else text[:MAX_OUTPUT] + "\n...[truncated]"


def approve(action: str) -> bool:
    if AUTO_APPROVE:
        return True
    return input(f"\n[approval needed] {action}\nAllow? [y/N] ").strip().lower() == "y"


# ---------- Tools ----------
def run_shell(command: str) -> str:
    if not approve(f"Run shell command: {command}"):
        return "User denied this command."
    try:
        r = subprocess.run(command, shell=True, capture_output=True, text=True, timeout=120)
        return clip(f"exit={r.returncode}\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}")
    except subprocess.TimeoutExpired:
        return "Command timed out after 120s."


def run_python(code: str) -> str:
    if not approve(f"Run Python code:\n{code}"):
        return "User denied this code."
    with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
        f.write(code)
        path = f.name
    try:
        r = subprocess.run([sys.executable, path], capture_output=True, text=True, timeout=120)
        return clip(f"exit={r.returncode}\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}")
    except subprocess.TimeoutExpired:
        return "Code timed out after 120s."
    finally:
        os.unlink(path)


def read_file(path: str) -> str:
    try:
        with open(path, "r", encoding="utf-8", errors="replace") as f:
            return clip(f.read())
    except Exception as e:
        return f"Error: {e}"


def write_file(path: str, content: str) -> str:
    if not approve(f"Write {len(content)} chars to {path}"):
        return "User denied this write."
    try:
        os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        return f"Wrote {path}"
    except Exception as e:
        return f"Error: {e}"


def list_dir(path: str = ".") -> str:
    try:
        return "\n".join(sorted(os.listdir(path))) or "(empty)"
    except Exception as e:
        return f"Error: {e}"


def fetch_url(url: str) -> str:
    try:
        r = requests.get(url, timeout=20, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer"]):
            tag.decompose()
        return clip(soup.get_text(separator="\n", strip=True))
    except Exception as e:
        return f"Error: {e}"


def web_search(query: str) -> str:
    try:
        r = requests.post(
            "https://html.duckduckgo.com/html/",
            data={"q": query},
            timeout=20,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        soup = BeautifulSoup(r.text, "html.parser")
        out = []
        for res in soup.select(".result")[:8]:
            a = res.select_one(".result__a")
            snip = res.select_one(".result__snippet")
            if a:
                out.append(f"{a.get_text(strip=True)}\n{a.get('href')}\n{snip.get_text(strip=True) if snip else ''}")
        return "\n\n".join(out) or "No results."
    except Exception as e:
        return f"Error: {e}"


TOOLS = {
    "run_shell": (run_shell, "Run a shell command and return its output.",
                  {"command": {"type": "string"}}),
    "run_python": (run_python, "Execute a Python script and return its output.",
                   {"code": {"type": "string"}}),
    "read_file": (read_file, "Read a text file.", {"path": {"type": "string"}}),
    "write_file": (write_file, "Create or overwrite a file.",
                   {"path": {"type": "string"}, "content": {"type": "string"}}),
    "list_dir": (list_dir, "List files in a directory.", {"path": {"type": "string"}}),
    "fetch_url": (fetch_url, "Fetch a web page and return its text.", {"url": {"type": "string"}}),
    "web_search": (web_search, "Search the web.", {"query": {"type": "string"}}),
}

TOOL_SCHEMAS = [
    {
        "name": name,
        "description": desc,
        "input_schema": {"type": "object", "properties": props, "required": list(props)},
    }
    for name, (_, desc, props) in TOOLS.items()
]


# ---------- Agent loop ----------
def run_agent(task: str, history: list) -> None:
    history.append({"role": "user", "content": task})
    for _ in range(MAX_STEPS):
        resp = client.messages.create(
            model=MODEL, max_tokens=4096, system=SYSTEM,
            tools=TOOL_SCHEMAS, messages=history,
        )
        history.append({"role": "assistant", "content": resp.content})

        for block in resp.content:
            if block.type == "text" and block.text.strip():
                print(f"\n{block.text}")

        if resp.stop_reason != "tool_use":
            return

        results = []
        for block in resp.content:
            if block.type == "tool_use":
                print(f"\n>> {block.name}({str(block.input)[:150]})")
                fn = TOOLS[block.name][0]
                try:
                    output = fn(**block.input)
                except Exception as e:
                    output = f"Tool error: {e}"
                results.append({"type": "tool_result", "tool_use_id": block.id, "content": output})
        history.append({"role": "user", "content": results})
    print("\n[stopped: reached max steps]")


def main() -> None:
    print("Agent ready. Type a task, or 'exit' to quit.")
    history: list = []
    while True:
        try:
            task = input("\nYou: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if task.lower() in {"exit", "quit"}:
            break
        if task:
            run_agent(task, history)


if __name__ == "__main__":
    main()