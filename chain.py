import json
from langchain_community.llms import Ollama
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableSequence, RunnableLambda
from whatsapp import send_whatsapp_message
import os
llm = Ollama(model="llama3.2")



extract_prompt = PromptTemplate.from_template("""
Extract the following from this email.

Return JSON in this format:
{{
  "mobile": "customer's phone number",
  "name": "customer's name or fallback to 'User'",
  "questions": ["list of customer questions"]
}}

EMAIL:
{email}
""")



reply_prompt = PromptTemplate.from_template("""
You're a WhatsApp support agent. Reply to customer named {name} based on these questions:
{questions}
Write a warm, helpful message, answering each question.
Sign off as "Team 360 Repair".
""")

def parse_llama_json(response):
    try:
        start = response.find("{")
        return json.loads(response[start:])
    except:
        return {"error": "LLM output malformed", "raw": response}

extract_chain = extract_prompt | llm | RunnableLambda(parse_llama_json)
reply_chain = reply_prompt | llm

def build_chain():
    return RunnableSequence(
        extract_chain,
        RunnableLambda(lambda data: {
            **data,
            "reply": reply_chain.invoke({
                "name": data.get("name", "User"),
                "questions": "\n".join(data.get("questions", []))
            })
        }),
        RunnableLambda(lambda data: {
            **data,
            "twilio_sid": send_whatsapp_message(data.get("mobile", os.getenv("TO_WHATSAPP_NUMBER")), data["reply"])
        })
    )
