import json
import os
from typing import Any

try:
    from google import genai
except ImportError:
    genai = None


DEFAULT_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")


def _client():
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key or genai is None:
        return None
    return genai.Client(api_key=api_key)


def ask_gemini(prompt: str, *, expect_json: bool = False) -> Any:
    """Call Gemini when configured. Return None when offline/unconfigured."""
    client = _client()
    if client is None:
        return None

    response = client.models.generate_content(
        model=DEFAULT_MODEL,
        contents=prompt,
    )
    text = (getattr(response, "text", None) or "").strip()

    if not expect_json:
        return text

    cleaned = text
    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "", 1).replace("```", "", 1).strip()

    try:
        return json.loads(cleaned)
    except json.JSONDecodeError:
        return None
