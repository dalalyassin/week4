from openai import OpenAI
from openai_helper import pprint_response, get_exchange_rate, tell_joke
from tools import first_tools, joke_tool
from dotenv import load_dotenv
import os
import json

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY environment variable is not set")

# Initialize OpenAI client
client = OpenAI(api_key=api_key)

# Available tool functions
available_tools = {
    "get_exchange_rate": get_exchange_rate,
    "tell_joke": tell_joke
}

def agent_loop(user_input: str, max_steps: int = 5):
    messages = [
        {"role": "system", "content": "You are a helpful assistant that can plan tasks and use tools."},
        {"role": "user", "content": user_input},
    ]

    for step in range(max_steps):
        print(f"\n=== Agent Step {step + 1} ===")

        # Step 1: Planner - decides next tool or response
        planner_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
            tools=first_tools + [joke_tool],
            tool_choice="auto"
        )
        planner_message = planner_response.choices[0].message
        pprint_response(planner_response)

        # Step 2: Executor - run any tool calls
        if planner_message.tool_calls:
            # Add assistant message with tool_calls first
            assistant_msg = {
                "role": "assistant",
                "content": planner_message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    }
                    for tc in planner_message.tool_calls
                ]
            }
            messages.append(assistant_msg)
            
            for tool_call in planner_message.tool_calls:
                tool_name = tool_call.function.name
                try:
                    args = json.loads(tool_call.function.arguments)
                    result = available_tools[tool_name](**args)
                except Exception as e:
                    result = f"Error executing {tool_name}: {e}"

                tool_result_str = str(result) if result is not None else ""

                print(f"Executed {tool_name} with result: {tool_result_str}")

                # Append tool result in proper format
                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": tool_result_str
                })

        else:
            # Step 3: Append assistant content safely
            assistant_content = planner_message.content or ""
            if assistant_content.strip():
                messages.append({
                    "role": "assistant",
                    "content": assistant_content
                })

        # Optional: stop if assistant says "done"
        last_content = messages[-1]["content"]
        if "done" in last_content.lower():
            break

    return messages[-1]["content"]

if __name__ == "__main__":
    prompt = input("Enter your prompt: ")
    response = agent_loop(prompt)
    print("\n=== Final Assistant Response ===")
    print(response)
