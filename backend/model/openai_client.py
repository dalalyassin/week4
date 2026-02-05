from openai import OpenAI
import os
from dotenv import load_dotenv
import logging

logger = logging.getLogger(__name__)

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)

def call_llm(prompt: str, temperature: float = 0.5, top_p: float = 0.5):
    logger.info(f"Calling OpenAI API - Temperature: {temperature}, Top_p: {top_p}")
    
    response = client.chat.completions.create(
        model="gpt-4o-mini",  
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=temperature,
        top_p=top_p
    )
    
    logger.info(f"OpenAI API call completed - Tokens used: {response.usage.total_tokens if response.usage else 'N/A'}")
    
    return response