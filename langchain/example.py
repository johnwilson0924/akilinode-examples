"""Use AkiliNode models in LangChain.

Install:  pip install langchain-openai
Get a key: https://akilinode.com/sign-up
"""

import os

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url="https://api.akilinode.com/v1",
    api_key=os.environ["AKILINODE_API_KEY"],
    model="deepseek-flash",  # any of the 25 AkiliNode models works
)

print(llm.invoke("Give me a one-line slogan for a Nairobi coffee shop.").content)
