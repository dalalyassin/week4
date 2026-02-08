# app/llm/client.py

from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

def call_llm(messages, tools=None):
    params = {
        "model": "gpt-4o-mini",
        "messages": messages,
    }
    if tools:
        params["tools"] = tools
        params["tool_choice"] = "auto"
    return client.chat.completions.create(**params)

