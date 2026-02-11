import requests

from config import OLLAMA_BASE_URL, OLLAMA_MODEL


def _normalize_base_url(base_url: str) -> str:
    return base_url.rstrip("/")


def _pick_default_model(base_url: str) -> str | None:
    try:
        resp = requests.get(f"{base_url}/api/tags", timeout=10)
        if resp.status_code != 200:
            return None

        data = resp.json()
        models = data.get("models", [])
        if not models:
            return None

        return models[0].get("name")
    except requests.RequestException:
        return None


def get_chat_message(prompt: str) -> str:
    if not OLLAMA_BASE_URL:
        return "Thieu OLLAMA_BASE_URL. Hay cau hinh trong file .env"

    base_url = _normalize_base_url(OLLAMA_BASE_URL)
    model = OLLAMA_MODEL or _pick_default_model(base_url)
    if not model:
        return "Khong tim thay model. Hay cai dat OLLAMA_MODEL hoac kiem tra /api/tags"

    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt,
            }
        ],
        "stream": False,
    }

    try:
        resp = requests.post(f"{base_url}/api/chat", json=payload, timeout=30)
        data = resp.json()
        if resp.status_code != 200:
            error = data.get("error") or data.get("message") or "Khong goi duoc Ollama."
            return f"Loi: {error}"

        message = data.get("message", {}).get("content")
        if not message:
            return "Ollama khong tra ve noi dung."

        return message
    except requests.RequestException:
        return "Khong the ket noi toi Ollama. Thu lai sau."
