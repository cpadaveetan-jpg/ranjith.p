from gemini_client import ask_gemini

def answer_question(question: str) -> str:
    prompt = f"""
You are EduGenie, a concise educational assistant.
Answer the student's question accurately and in simple language.
Question: {question}
"""
    answer = ask_gemini(prompt)
    if answer:
        return answer

    # Offline fallback so the project still runs without an API key.
    return (
        "Gemini API is not configured. Add GEMINI_API_KEY to your .env file "
        "for AI-powered answers. Your question was: " + question
    )
