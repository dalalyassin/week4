import json
from prompt import PROMPT
from openai_sdk import OpenAIProvider
from local_model import LocalLlamaProvider
from gemini import GeminiProvider

def run(provider_name: str, provider):
    print(f"\n=== Running with {provider_name} ===")

    try:
        raw = provider.generate(PROMPT)
        print("RAW OUTPUT:")
        print(raw)

        try:
            parsed = json.loads(raw)
            print("PARSED OUTPUT:")
            print(parsed)
        except json.JSONDecodeError:
            print("Could not parse output as JSON. Raw text above.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    from dotenv import load_dotenv
    import os

    load_dotenv()

    providers = {
        "openai": OpenAIProvider(os.getenv("OPENAI_API_KEY")),
        "llama.cpp": LocalLlamaProvider("models/mistral-7b-instruct-v0.2.Q4_K_M.gguf"),
        "gemini": GeminiProvider(os.getenv("GEMINI_API_KEY")),
    }


    for name, provider in providers.items():
        run(name, provider)
