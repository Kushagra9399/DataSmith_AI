from fastapi import APIRouter, UploadFile, File, Form
import os
import shutil
import uuid

from services.file_service import extract_content
from agents.intent_agent import detect_intent
from agents.executor_agent import execute_task
from utils.memory import conversation_context

router = APIRouter()

UPLOAD_DIR = "uploads"

os.makedirs(UPLOAD_DIR, exist_ok=True)


@router.post("/process")
async def process_input(
    text: str = Form(default=""),
    session_id: str = Form(default=""),
    file: UploadFile = File(default=None)
):

    extracted_text = ""

    logs = []

    if not session_id:
        session_id = str(uuid.uuid4())
        conversation_context[session_id] = []
        logs.append(f"New Session ID created: {session_id}")
        print(f"Session ID: {session_id}")
    
    if session_id not in conversation_context:
        conversation_context[session_id] = []

    if file:
        file_path = f"{UPLOAD_DIR}/{file.filename}"

        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        logs.append(f"File uploaded: {file.filename}")

        extracted_text = extract_content(file_path)

        logs.append("Content extracted successfully")
    
    elif text:
        extracted_text = extract_content(
            text=text
        )

        logs.append(
            "Text/URL processed successfully"
        )

    if text:
        extracted_text += f"\n{text}"

    if not extracted_text.strip():
        return {
            "error": "No input provided",
            "session_id": session_id
        }
    
    conversation_context[session_id].append({
        "role": "user",
        "content": extracted_text
    })

    print("Extracted text:")
    print(extracted_text)

    history = ""

    history = "\n".join([conversation["role"]+": "+conversation["content"] for conversation in conversation_context[session_id]])

    intent_result = detect_intent(extracted_text, history)

    print(intent_result)

    logs.append(f"Intent detected: {intent_result['intent']}")

    if intent_result["needs_followup"]:

        conversation_context[session_id].append({
            "role": "assistant",
            "content": intent_result["reasoning"] + ".".join(intent_result["questions"])
        })

        return {
            "follow_up_question": intent_result["questions"],
            "logs": logs,
            "session_id": session_id
        }
    
    if intent_result["intent"] == "question_answering":    
        conversation_context[session_id].append({
            "role": "assistant",
            "content": intent_result["reasoning"] + "\n" + intent_result["answer"]
        })
        return {
            "intent": intent_result["intent"],
            "extracted_text": extracted_text,
            "result": intent_result["answer"],
            "logs": logs,
            "session_id": session_id
        }

    result = execute_task(
        intent=intent_result["intent"],
        text=history+"\n"+extracted_text
    )

    logs.append("Task executed successfully")
    
    conversation_context[session_id].append({
            "role": "assistant",
            "content": result
    })
    
    return {
        "intent": intent_result["intent"],
        "extracted_text": extracted_text,
        "result": result,
        "logs": logs,
        "session_id": session_id
    }