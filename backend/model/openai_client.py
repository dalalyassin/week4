from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)


def call_llm(prompt: str) -> str:
    """
you're a helpful assistant that can use tools to help the user find out the exchange rate of a currency. 
   """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )
    return response.choices[0].message.content

if __name__ == "__main__":
    prompt = input("Enter a prompt: ")
    answer = call_llm(prompt)
    print(answer)