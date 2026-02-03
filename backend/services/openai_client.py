from openai import OpenAI
import os
from prompts.stress_test import stress_test_prompt
from dotenv import load_dotenv
from schemas.base import PromptRequest
from services.temp_storage import test_messages_storage
import logging

load_dotenv()

logger = logging.getLogger(__name__)

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)


# SYSTEM_PROMPT 
def call_llm(req: PromptRequest):
    # Handle None session_id
    session_id = req.session_id or "default"
    prompt = req.prompt
    
    logger.info(f"Session ID: {session_id}, Storage keys: {list(test_messages_storage.keys())}")
    
    #initialize the session if it doesn't exist
    if session_id not in test_messages_storage:
        logger.info(f"Creating new session: {session_id}")
        test_messages_storage[session_id] = [
            {"role": "system", "content": stress_test_prompt}
        ]
    else:
        logger.info(f"Using existing session: {session_id} with {len(test_messages_storage[session_id])} messages")
    
    # Add user message to conversation history
    test_messages_storage[session_id].append({"role": "user", "content": prompt})
    
    # Get all messages including system prompt and history
    messages = test_messages_storage[session_id]
    logger.info(f"Sending {len(messages)} messages to OpenAI (session: {session_id})")
    
    # Call OpenAI API
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  
        messages=messages
    )
    
    # Add assistant response to conversation history
    assistant_content = response.choices[0].message.content
    test_messages_storage[session_id].append({"role": "assistant", "content": assistant_content})
    logger.info(f"Session {session_id} now has {len(test_messages_storage[session_id])} messages")
    
    return response