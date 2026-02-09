from openai import OpenAI

from openai_helper import pprint_response, get_exchange_rate
from tools import first_tools
from dotenv import load_dotenv
import os
import json

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

client = OpenAI(api_key=api_key)


def llm_conversation(user_input: str):
    messages = [
        {
            "role": "system",
            "content": "You are a helpful assistant that can use tools to help the user find out the exchange rate of a currency.",
            "tools": first_tools,
        },
    ]

    available_tools = {"get_exchange_rate": get_exchange_rate}
    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=first_tools,
        tool_choice="auto",
    )

    pprint_response(response)
    print("--------------------------------")
    
    if response.choices[0].message.tool_calls:
        messages.append(
            {
                "role": "assistant",
                "content": response.choices[0].message.content or "",
                "tool_calls": response.choices[0].message.tool_calls,
            }
        )

        for tool_call in response.choices[0].message.tool_calls:
            tool_name = tool_call.function.name
            tool_call_id = tool_call.id

            try:
                tool_arguments = json.loads(tool_call.function.arguments)
                tool_response = available_tools[tool_name](**tool_arguments)
            except Exception as e:
                tool_response = f"Tool execution failed: {str(e)}"

            messages.append(
                {
                    "role": "tool",
                    "content": str(tool_response),
                    "tool_call_id": tool_call_id,
                }
            )

            response = client.chat.completions.create(
                model="gpt-4o",
                messages=messages,
                tools=first_tools,
                tool_choice="auto",
            )
            return response

    else:
        return response


if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    response = llm_conversation(prompt)
    pprint_response(response)
