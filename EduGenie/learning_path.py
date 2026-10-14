from gemini_client import ask_gemini

def get_learning_recommendations(topic: str) -> str:
    prompt = f"""
Create a personalized learning path for the topic "{topic}".
Organize it from beginner to advanced.
Include suggested order, practice ideas, and useful resource types
(videos, articles, or books). Keep it practical and clear.
"""
    answer = ask_gemini(prompt)
    if answer:
        return answer

    return (
        f"Learning path for {topic}\n\n"
        "1. Beginner: Learn definitions and core concepts.\n"
        "2. Intermediate: Study worked examples and practice exercises.\n"
        "3. Advanced: Build a small project and solve application problems.\n"
        "4. Revision: Test yourself and review weak areas.\n\n"
        "Configure GEMINI_API_KEY for personalized Gemini recommendations."
    )
