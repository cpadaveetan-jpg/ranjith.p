# EduGenie: Google Gemini Powered Learning Assistant

A FastAPI + HTML/CSS implementation of the EduGenie project described in the supplied Naan Mudhalvan project document.

## Features

- QnA
- Concept explanation
- Quiz generation: 3 MCQs with 4 options
- Summarization
- Personalized learning recommendations
- Simple responsive web interface

## Folder structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── requirements.txt
├── .env.example
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css
```

## Run in VS Code

Open the EduGenie folder in VS Code.

### Windows

```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
uvicorn main:app --reload
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
uvicorn main:app --reload
```

Open:

http://127.0.0.1:8000

## Gemini API

To use live AI responses, put your Gemini API key in `.env`:

```env
GEMINI_API_KEY=your_real_key
GEMINI_MODEL=gemini-2.5-flash
```

If no key is configured, the application still starts and uses safe offline fallback responses. This makes it easy to demonstrate the interface before adding the API key.

## Documented API endpoints

- POST `/qa`
- POST `/explain`
- POST `/quiz`
- POST `/summarize`
- POST `/learn/recommendations`

There is also `/api/task` for the frontend dispatcher.

## Important

The supplied project document names Gemini 1.5 Pro and LaMini-Flan-T5. This implementation keeps the same module architecture and functionality, but uses a configurable current Gemini model through the official `google-genai` SDK. The explanation module keeps a local fallback rather than downloading a large local model automatically.
