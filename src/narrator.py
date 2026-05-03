"""
把 stats dict 喂给 LLM,返回一段自然语言总结。
用 prompts/narrate.md 模板。
"""

import json
import httpx
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent.parent / "prompts"

def _load_template(name: str) -> str:
    """从 prompts/ 加载一个 .md 文件,返回内容字符串。"""
    return (PROMPTS_DIR / name).read_text(encoding="utf-8")

def narrate(
    stats: dict,
    endpoint: str = "http://localhost/v1/chat/completions:11434",
    model: str = "qwen3:14b",
    prompt_file: str = "narrate.md",
) -> str:
    stats_json = json.dumps(stats, ensure_ascii=False, indent=2)
    prompt = _load_template(prompt_file)
    prompt = prompt.replace("[[STATS]]", stats_json)

    headers = {
        "Authorization": "Bearer ollama",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "stream": False,
    }
    resp = httpx.post(endpoint, headers=headers, json=payload, timeout=120)
    resp.raise_for_status()
    return resp.json()["choices"][0]["message"]["content"]