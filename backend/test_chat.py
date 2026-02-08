# test_chat.py
# Test script for exchange currency functionality

from app.routers.chat import handle_chat

if __name__ == "__main__":
    input_prompt = input("Enter your prompt: ")
    prompt = f"Please respond to the following prompt: {input_prompt}"
    result = handle_chat(prompt)
    print(f"Response: {result}")

