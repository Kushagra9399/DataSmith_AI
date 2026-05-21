from services.summarizer import summarize_text
from services.sentiment import analyze_sentiment
from services.code_explainer import explain_code


def execute_task(intent, text):

    if intent == "summarization":
        return summarize_text(text)

    elif intent == "sentiment_analysis":
        return analyze_sentiment(text)

    elif intent == "code_explanation":
        return explain_code(text)

    else:
        return {
            "response": text
        }