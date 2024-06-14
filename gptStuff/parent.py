import json
import os
from openai import OpenAI
from dotenv import load_dotenv


from obsidianScripts.main import main

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def parent(prompt,client):
    print('inside parent',prompt)

    with open("gptStuff/SystemPrompts/parentSystemPrompt.txt") as f:
        systemPrompt = f.read()
    chat_completion = client.chat.completions.create(
        messages=[
            {"role":"system","content":systemPrompt},
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="gpt-3.5-turbo",
        response_format={ "type": "json_object" }
    )
    parentResult = json.loads(chat_completion.choices[0].message.content)
    print(parentResult)
    return parentResult