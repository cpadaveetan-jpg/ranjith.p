from gemini_client import ask_gemini

def explain_topic(topic: str) -> str:
    prompt = f"""
Explain the following educational topic for a beginner.
Use simple language, a short definition, key points, and one example.
Topic: {topic}
"""
    answer = ask_gemini(prompt)
    if answer:
        return answer

    return (
        f"Offline explanation for '{topic}':\n\n"
        f"Start by learning the definition of {topic}, its main ideas, "
        "and one practical example. Configure GEMINI_API_KEY to receive "
        "a full AI-generated explanation."
    )
