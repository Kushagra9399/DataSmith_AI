import os
from groq import Groq
from dotenv import load_dotenv
import re
import json

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def detect_intent(text, history):
    print("History: ", history)
    prompt = (
    """
    You are an AI intent detection agent.

    Analyze the user input and the conversation history.

    Possible intents:
    - summarization
    - sentiment_analysis
    - code_explanation
    - question_answering

    OUTPUT JSON:
    {
        "needs_followup": true,
        "questions": [
            "question_1",
            "question_2"
        ],
        "intent": "",
        "confidence": 0.5,
        "reasoning": "",
        "answer": ""
    }

    Rules:
    - If intent is unclear, ask follow-up question.
    - Max of 2 questions can be asked it intent is not clear.
    - Ask only what is required not the explaination.
    - You can ask like "what to do with the given code", "Do you need summary of this or you have some questions".
    - If intent is of "question_answering", then provide answer in "answer" value.
    - Return JSON only.
    """
    f"\nConversation History: {history}"
    f"\nUser Input: {text}"
    )

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.1
    )

    output = response.choices[0].message.content
    cleaned = re.sub(r"^```json\s*|\s*```$", "", output.strip(), flags=re.DOTALL)
    cleaned = re.sub(r"^```\s*|\s*```$", "", cleaned.strip(), flags=re.DOTALL)
    print(output)
    print(cleaned)
    try:
        data = json.loads(cleaned)
        return data

    except Exception as e:
        return {
            "intent": "question_answering",
            "needs_followup": False,
            "question": "",
            "error": str(e),
            "answer": ""
        }