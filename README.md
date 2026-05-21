
# Agentic AI Assistant Application

An intelligent multimodal AI assistant built using **FastAPI**, **Groq LLMs**, and a lightweight frontend.  
The system can process:

- Text input
- Images (OCR)
- PDFs
- Audio files
- YouTube URLs

It supports:
- Session-based conversation memory
- Follow-up question handling
- Intent detection
- AI task orchestration
- Markdown rendering
- Context-aware responses

---

# Features

## Multimodal Input Support

The application accepts:

- Plain text
- Image uploads (`png`, `jpg`, `jpeg`)
- PDF files
- Audio files (`mp3`, `wav`, `m4a`)
- YouTube video links

---

## AI Capabilities

The system automatically detects user intent and performs tasks such as:

- Summarization
- Sentiment Analysis
- Code Explanation
- General Question Answering

---

## Agentic Workflow

The application behaves like an AI agent:

- Detects ambiguous requests
- Asks follow-up questions
- Stores session memory
- Uses previous conversation context
- Executes the final task intelligently

---

# Tech Stack

## Frontend

- HTML
- CSS
- JavaScript
- Markdown Rendering (`marked.js`)
- Fetch API

## Backend

- FastAPI
- Python
- REST API
- Session Memory Management

## AI / LLM

- Groq API
- Llama 3.3 70B Versatile

## OCR & Parsing

- pytesseract
- PyMuPDF
- SpeechRecognition
- youtube-transcript-api

---

# Project Architecture

![Architecture Diagram](Gemini_Generated_Image_4dtake4dtake4dta.png)

---

# System Workflow

## 1. User Sends Input

The user can:
- Type text
- Upload a file
- Provide a YouTube URL

---

## 2. Frontend Sends Request

Frontend sends:
- text
- uploaded file
- session_id

to the FastAPI backend using `POST /process`.

---

## 3. Backend Processes Input

The backend:
- detects file type
- extracts content
- fetches transcripts if YouTube URL detected

---

## 4. Session Memory Handling

A unique `session_id` is created using UUID.

Conversation history is stored in:

```python
conversation_store = {}
```

This allows:
- contextual understanding
- follow-up reasoning
- memory-based responses

---

## 5. Intent Detection Agent

The extracted content + conversation history are sent to the Groq LLM.

The AI detects:
- summarization
- sentiment_analysis
- code_explanation
- question_answering

If the request is unclear:
- AI asks follow-up questions

---

## 6. Task Execution Layer

Based on intent:

| Intent | Service |
|---|---|
| summarization | summarizer.py |
| sentiment_analysis | sentiment.py |
| code_explanation | code_explainer.py |
| question_answering | generic response |

---

## 7. Response Generation

The AI response is:
- formatted
- converted to markdown
- shown in chat UI

---

# Folder Structure

```text
project-root/
│
├── backend/
│   ├── agents/
│   │   ├── intent_agent.py
│   │   └── executor_agent.py
│   │
│   ├── routes/
│   │   └── process.py
│   │
│   ├── services/
│   │   ├── file_service.py
│   │   ├── pdf_service.py
│   │   ├── ocr_service.py
│   │   ├── audio_service.py
│   │   ├── youtube_service.py
│   │   ├── summarizer.py
│   │   ├── sentiment.py
│   │   └── code_explainer.py
│   │
│   ├── utils/
│   │   └── memory.py
│   │
│   ├── uploads/
│   ├── app.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md
```

---

# Installation & Setup

# 1. Clone Repository

```bash
git clone <your-github-repo-url>
cd <project-folder>
```

---

# 2. Create Virtual Environment

## Linux / Mac

```bash
python3 -m venv venv
source venv/bin/activate
```

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

---

# 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 4. Install Tesseract OCR

## Ubuntu / Linux

```bash
sudo apt update
sudo apt install tesseract-ocr
```

Verify installation:

```bash
tesseract --version
```

---

# 5. Create `.env`

Inside `backend/`

Create:

```env
GROQ_API_KEY=your_groq_api_key
```

---

# Getting Groq API Key

## Step 1

Open:

https://console.groq.com

## Step 2

Create account/login.

## Step 3

Go to:
- API Keys
- Create API Key

## Step 4

Copy the key and paste into `.env`.

---

# Running the Backend

Inside `backend/`

```bash
uvicorn app:app --reload
```

Backend runs at:

```text
http://127.0.0.1:8000
```

Swagger Docs:

```text
http://127.0.0.1:8000/docs
```

---

# Running the Frontend

Inside `frontend/`

Open:

```text
index.html
```

OR use VS Code Live Server.

---

# API Endpoint

## POST `/process`

Accepts:
- text
- file
- session_id

Returns:
- AI result
- follow-up question
- logs
- session id

---

# Supported Inputs

| Type | Supported |
|---|---|
| Text | Yes |
| Image OCR | Yes |
| PDF Parsing | Yes |
| Audio Transcription | Yes |
| YouTube Transcript | Yes |

---

# YouTube Transcript Flow

If a YouTube URL is detected:

1. Extract video ID
2. Fetch transcript
3. Convert transcript to text
4. Send transcript to AI pipeline

Fallback message shown if transcript unavailable.

---

# Session Memory System

The application uses:

```python
conversation_store = {}
```

Each user session:
- receives unique UUID
- stores previous messages
- enables contextual reasoning

This allows:

```text
User: Summarize this PDF
AI: Which type of summary?
User: Bullet summary
```

The AI understands the second message using stored context.

---

# Logging & Explainability

The backend generates logs such as:
- file uploaded
- OCR completed
- transcript fetched
- intent detected
- task executed

Useful for:
- debugging
- explainability
- assignment demonstration

---

# Future Improvements

Potential enhancements:

- PostgreSQL integration
- Redis session memory
- Vector database
- RAG pipeline
- LangChain orchestration
- Authentication system
- Cloud storage
- Multi-agent workflows
- Streaming responses
- Docker deployment

---

# Deployment

## Frontend

Can be deployed on:
- Vercel
- Netlify

## Backend

Can be deployed on:
- Render
- Railway
- AWS
- Azure

---

# Example Use Cases

## PDF Summarization

Upload PDF → AI generates summary.

---

## Code Explanation

Upload code screenshot or paste code → AI explains logic.

---

## Sentiment Analysis

Upload customer review → AI detects sentiment.

---

## YouTube Video Summary

Paste YouTube URL → AI summarizes transcript.

---

# Author

Developed as an Agentic AI Assignment Project using:
- FastAPI
- Groq
- OCR
- Session Memory
- Multimodal AI Processing
