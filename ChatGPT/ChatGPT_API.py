"""
First simple program more to come
ChatGPT_API.py
Peter Dinh
"""

import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", 
messages=[{"role": "user", "content": "Write an essay about Vietnam "}])
print(completion.choices[0].message.content)