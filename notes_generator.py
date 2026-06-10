from chatbot import get_ai_response

def generate_notes(prompt):

    messages = [
        {
            "role": "user",
            "content": f"""
            Create clean study notes for this topic.

            Topic:
            {prompt}

            Format:
            - Title
            - Definition
            - Key Points
            - Advantages
            - Applications
            - Short Summary

            Give output in neat notes format.
            """
        }
    ]

    return get_ai_response(messages)
