from gemini_client import ask_gemini

def summarize_text(text: str) -> str:
    prompt = f"""
Summarize the following educational text into a concise, easy-to-understand
revision note. Keep the important information and remove repetition.
Text:
{text}
"""
    answer = ask_gemini(prompt)
    if answer:
        return answer

    # Simple deterministic fallback.
    sentences = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
    if len(sentences) <= 3:
        return ". ".join(sentences) + ("." if sentences else "Please provide text.")
    return ". ".join(sentences[:3]) + ".\n\n(Gemini API is not configured; this is the offline fallback.)"
