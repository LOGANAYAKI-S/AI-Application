from groq import Groq

client = Groq(
    api_key="your-key"
)

question = input("Ask something: ")

chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": question,
        }
    ],
    model="llama-3.1-8b-instant",
)

print("\nAI Answer:")
print(chat_completion.choices[0].message.content)


output
Ask something: what is tree?

AI Answer:
A tree is a perennial plant with an elongated stem, or trunk, which supports branches and leaves in most cases, as well as in some cases producing flowers, fruits, and seeds. Trees are among the oldest and largest living organisms found on Earth, and they serve various ecological roles.
