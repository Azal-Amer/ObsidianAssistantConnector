import json
import os
from openai import OpenAI
from dotenv import load_dotenv


from obsidianScripts.main import main

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")


def brother(informationForBrother,parentResult,client):
    with open("gptStuff/SystemPrompts/brotherSystemPrompt.txt") as f:
        prompt = f.read()   
    
    brotherContext = parentResult["brother"]["context"]
    brotherPrompt = brotherContext + "\n<informationForBrother>" + informationForBrother + "\n</informationForBrother>"
    print('brotherPrompt',brotherPrompt)

    chat_completion = client.chat.completions.create(
        messages=[
            {"role":"system","content":prompt},
            {
                "role": "user",
                "content": brotherPrompt,
            }
        ],
        model="gpt-4o"
)
    finalOutput = chat_completion.choices[0].message.content
    return finalOutput