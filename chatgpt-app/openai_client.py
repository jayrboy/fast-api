import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

async def ask_gpt(messages):
    response = openai.ChatCompletion.create(
        model="gpt-3.5",
        messages=messages
    )
    return response['choices'][0]['message']['content']
