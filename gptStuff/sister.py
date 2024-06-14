import json
import os
from openai import OpenAI
from dotenv import load_dotenv


from obsidianScripts.main import main

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
def sister(parentResult,client):
    sisterPrompt = parentResult["sister"]["details"]
    with open("gptStuff/SystemPrompts/sisterSystemPrompt.txt") as f:
        prompt = f.read()
    

    chat_completion = client.chat.completions.create(
        messages=[
            {"role":"system","content":prompt},
            {
                "role": "user",
                "content": sisterPrompt,
            }
        ],
        model="gpt-3.5-turbo",
        response_format={ "type": "json_object" }
    )
    result = json.loads(chat_completion.choices[0].message.content)
    print('sister result',result)

    answers = []

    currentPerson = ''
    if result['type']=='list':
        for item in result['content']:
            if item['person'] != currentPerson:
                if currentPerson != '':
                    answers.append(f"</{currentPerson}>")
                currentPerson = item['person']
                answers.append(f"\n<{currentPerson}>")
            answers.append(main(json_data=item,debug=False,safemode=True,hotword='store'))
    else:
        answers.append(main(json_data=result,debug=False,safemode=True,hotword='store'))
    # now combine the answers into a single string with line breaks and print it
    try:
        informationForBrother = "\n".join(answers)
    except:
        informationForBrother = "There was no information to report back to the brother"
    print(informationForBrother)


    return informationForBrother
