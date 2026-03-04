import os
import json
from groq import Groq
from agent.tools import web_search, tools_list
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def run_agent(question: str) -> str:
    messages = [
        {
            "role": "system",
            "content": "You are a helpful research assistant. Use the web_search tool to find current information before answering. Always search first, then synthesize the results into a clear answer."
        },
        {"role": "user", "content": question}
    ]

    # Agentic loop
    while True:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=messages,
            tools=tools_list,
            tool_choice="auto",
            temperature=0
        )

        msg = response.choices[0].message

        # If no tool call, we have the final answer
        if not msg.tool_calls:
            return msg.content

        # Process tool calls
        messages.append({
            "role": "assistant",
            "content": msg.content or "",
            "tool_calls": [
                {
                    "id": tc.id,
                    "type": "function",
                    "function": {
                        "name": tc.function.name,
                        "arguments": tc.function.arguments
                    }
                } for tc in msg.tool_calls
            ]
        })

        for tc in msg.tool_calls:
            args = json.loads(tc.function.arguments)
            result = web_search(args["query"])
            messages.append({
                "role": "tool",
                "tool_call_id": tc.id,
                "content": result
            })