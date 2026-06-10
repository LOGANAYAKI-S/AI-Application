from modules.chatbot import get_ai_response

def explain_code(prompt):

    messages = [
        {
            "role": "user",
            "content": f"""
            Explain this programming code clearly
            in simple beginner-friendly steps.

            Code:
            {prompt}
            """
        }
    ]

    return get_ai_response(messages)