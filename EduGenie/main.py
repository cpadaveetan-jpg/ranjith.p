from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from qna import answer_question
from explanation_module import explain_topic
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie: Google Gemini Powered Learning Assistant")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/qa")
async def qa(payload: dict):
    question = (payload.get("question") or "").strip()
    if not question:
        return JSONResponse({"error": "Please enter a question."}, status_code=400)
    return {"answer": answer_question(question)}


@app.post("/explain")
async def explain(payload: dict):
    topic = (payload.get("topic") or "").strip()
    if not topic:
        return JSONResponse({"error": "Please enter a topic."}, status_code=400)
    return {"explanation": explain_topic(topic)}


@app.post("/quiz")
async def quiz(payload: dict):
    passage = (payload.get("passage") or "").strip()
    if not passage:
        return JSONResponse({"error": "Please enter a topic or passage."}, status_code=400)
    return {"quiz": generate_quiz(passage)}


@app.post("/summarize")
async def summarize(payload: dict):
    text = (payload.get("text") or "").strip()
    if not text:
        return JSONResponse({"error": "Please enter text to summarize."}, status_code=400)
    return {"summary": summarize_text(text)}


@app.post("/learn/recommendations")
async def learning_recommendations(payload: dict):
    topic = (payload.get("topic") or "").strip()
    if not topic:
        return JSONResponse({"error": "Please enter a learning topic."}, status_code=400)
    return {"recommendations": get_learning_recommendations(topic)}


@app.post("/api/task")
async def task(payload: dict):
    """Single frontend-friendly endpoint that dispatches to the five documented modules."""
    task_name = (payload.get("task") or "").strip().lower()
    text = (payload.get("text") or "").strip()

    if not text:
        return JSONResponse({"error": "Please enter some input."}, status_code=400)

    if task_name in {"qa", "qna", "question"}:
        return {"result": answer_question(text)}
    if task_name in {"explain", "explanation"}:
        return {"result": explain_topic(text)}
    if task_name == "quiz":
        return {"result": generate_quiz(text)}
    if task_name in {"summary", "summarize"}:
        return {"result": summarize_text(text)}
    if task_name in {"recommend", "recommend path", "learning path", "recommendations"}:
        return {"result": get_learning_recommendations(text)}

    return JSONResponse(
        {"error": "Unknown task. Choose Explain, QnA, Quiz, Summary, or Recommend Path."},
        status_code=400,
    )
