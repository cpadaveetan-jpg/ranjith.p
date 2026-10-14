from gemini_client import ask_gemini

def generate_quiz(passage: str):
    prompt = f"""
Create exactly 3 multiple-choice questions from the passage below.
Each question must have exactly 4 options and one correct answer.
Return ONLY valid JSON in this format:
[
  {{"question":"...", "options":["A","B","C","D"], "answer":"A"}}
]
Passage:
{passage}
"""
    result = ask_gemini(prompt, expect_json=True)
    if isinstance(result, list) and len(result) == 3:
        return result

    return [
        {
            "question": "Is Gemini API configured?",
            "options": ["Yes", "No", "Not checked", "Unknown"],
            "answer": "Not checked",
        },
        {
            "question": "Which EduGenie feature generates MCQs?",
            "options": ["Quiz", "CSS", "Uvicorn", "Jinja2"],
            "answer": "Quiz",
        },
        {
            "question": "How many questions does the documented quiz feature generate?",
            "options": ["1", "2", "3", "5"],
            "answer": "3",
        },
    ]
