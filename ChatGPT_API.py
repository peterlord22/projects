"""
ChatGPT_API.py
Peter Dinh
"""

pip install -q openai

openai.api_key = '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'

import openai

messages = [
    {"role": "system". "content": "You are a kind helpful assistant."},
]

while True: 
    message - input("User: ")
    if message: 
        messages.append(
             {"role": "system". "content": message},
        )
        chat = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo", messages = messages
        )

    reply = chat.choices[0].message.content
    print(f"ChatGPT: {reply}")
    messages.append({"role": "system". "content": reply})
