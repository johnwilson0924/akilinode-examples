"""AkiliNode quickstart (Python).

Works with the standard OpenAI Python SDK — the only changes are
base_url and api_key.

Install:  pip install openai
Get a key: https://akilinode.com/sign-up
"""

import os

from openai import OpenAI

client = OpenAI(
    base_url="https://api.akilinode.com/v1",
    api_key=os.environ["AKILINODE_API_KEY"],  # your AkiliNode token
)

resp = client.chat.completions.create(
    model="deepseek-flash",  # or deepseek-v4-pro, glm-5.3, qwen3.7-max, ...
    messages=[
        {"role": "user", "content": "Explain M-Pesa to a developer in one sentence."},
    ],
)

print(resp.choices[0].message.content)
