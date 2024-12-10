import os
import re
import hashlib
import ast
from openai import AzureOpenAI
from datetime import date

# openai_key = os.getenv("OPENAI_API_KEY")
# print(openai_key)


trapi_deployment_list = [
    'gpt-35-turbo',
    # 'gpt-35-turbo-16k',
    # 'gpt-35-turbo-instruct',
    # 'gpt-4',
    # 'gpt-4-32k',
    # 'gpt-4o',
    # 'gpt-4o-mini',
    # 'gpt-4-turbo',
    # 'gpt-4-turbo-v'
]

deployment = trapi_deployment_list[0]
TRAPI_END_POINT = 'gcr/shared'
TRAPI_BASE_URL = 'https://trapi.research.microsoft.com/' + TRAPI_END_POINT
TRAPI_API_VERSION = '2024-02-01'
# TRAPI_API_KEY = os.getenv("TRAPI_API_KEY") # contant your mentor for the key
TRAPI_API_KEY = "cd2caafdcf2e4f3f97474e55bd3d4d0a"

client = AzureOpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    api_version=TRAPI_API_VERSION,
    azure_endpoint=TRAPI_BASE_URL,
    azure_deployment=deployment
)

monthDay = date.today().strftime("%B %d")

retry = 0
response = client.chat.completions.create(
        model=deployment,
        
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role":"user",
                "content": "Today is " +  monthDay + ".  Select one historical fact for the day at random and write a 2-stanza poem about it.",
            }
        ],
        max_tokens=500
    )

print(deployment, response.choices[0].message.content)
print('-'*8)
if response and 'choices' in response.json():
    print("ok")