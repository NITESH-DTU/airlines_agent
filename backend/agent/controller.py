from services.all_tools import tool_functions,tools
import os
from dotenv import load_dotenv
from openai import OpenAI
import json
load_dotenv(override=True)
gemini_api=os.getenv("GEMINI_API_KEY");
gemini=OpenAI(
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=gemini_api
)

def system_prompt():
    return f"""You are an AI flight booking assistant.

    Your job is to help users with:
    - searching flights
    - booking flights
    - handling payments (simulated)
    - answering basic airline-related questions

    IMPORTANT RULES:
    - Do NOT assume real-time data
    - Do NOT generate real flight schedules or prices
    - Use only placeholder or dummy information when needed

    Always:
    - Understand the user’s intent clearly
    - Respond in a helpful and concise way
    - Ask follow-up questions if information is missing (like date, source, destination)

    If the user asks about policies (baggage, cancellation, etc.), give general answers, not airline-specific facts.

    If you don’t know something, say:
    "I’m not sure about that yet, but I can help with booking or searching flights."

    Keep responses natural and conversational."""
sys=system_prompt()
history=[{"role":"system","content":sys}]
print(gemini_api)
def chat(message:str):
    global history
    history.append({"role":"user","content":message})
    messages=history
    response = gemini.chat.completions.create(
        model="gemini-2.5-flash",
        messages=messages,   
        tools=tools
    )
    
    while getattr(response.choices[0].message, "tool_calls", None):

        assistant_message = response.choices[0].message

        assistant_dict = {
            "role": "assistant",
            "content": assistant_message.content or "",
            "tool_calls": assistant_message.tool_calls
        }

        history.append(assistant_dict)
        messages.append(assistant_dict)

        responses = handle_tool_call(assistant_message)

        history.extend(responses)
        messages.extend(responses)

        response = gemini.chat.completions.create(
            model="gemini-2.5-flash",
            messages=messages,
            tools=tools
        )

    final_msg = response.choices[0].message

    history.append({
    "role": "assistant",
    "content": final_msg.content
    })

    return final_msg.content
    
def handle_tool_call(message):
    responses=[]
    for tool_call in message.tool_calls:
        if tool_call.function.name in tool_functions:
            arguments=json.loads(tool_call.function.arguments)
            func=tool_functions[tool_call.function.name]
            result=func(**arguments)
            responses.append({
                "role":"tool",
                "tool_call_id":tool_call.id,
                "name":tool_call.function.name,
                "content":str(result)
            })
    return responses
    