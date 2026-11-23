import json
import os
import urllib.request


def ask_json(system, payload, model):
    base = os.getenv("LLM_BASE_URL", "http://127.0.0.1:11434/v1").rstrip("/")
    headers = {"Content-Type": "application/json"}
    if os.getenv("LLM_API_KEY"):
        headers["Authorization"] = "Bearer " + os.environ["LLM_API_KEY"]
    body = {"model": model, "stream": False, "response_format": {"type": "json_object"},
            "messages": [{"role": "system", "content": system},
                         {"role": "user", "content": json.dumps(payload)}]}
    request = urllib.request.Request(base + "/chat/completions", data=json.dumps(body).encode(), headers=headers)
    with urllib.request.urlopen(request, timeout=120) as response:
        result = json.load(response)
    return json.loads(result["choices"][0]["message"]["content"])
