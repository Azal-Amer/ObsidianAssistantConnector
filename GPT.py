import json
import os
from openai import OpenAI
from dotenv import load_dotenv


from obsidianScripts.main import main


load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")
# get the api key from the environment
model_engine = "text-davinci-002"  # Specify the GPT-3.5 model engine
max_tokens = 50  # Adjust the maximum number of tokens in the response
temperature = 0.7  # Adjust the creativity of the response (0.0 to 1.0)

with open("gptStuff/systemPrompt.txt") as f:
    prompt = f.read()
prompt
client = OpenAI(
    # This is the default and can be omitted
    api_key=openai_api_key
)
chat_completion = client.chat.completions.create(
    messages=[
        {"role":"system","content":prompt},
        {
            "role": "user",
            "content": "Abeera likes to read books and she is a good student. She's my best friend.",
        }
    ],
    model="gpt-3.5-turbo",
    response_format={ "type": "json_object" }
)
print(chat_completion)

result = chat_completion.choices[0].message["content"]

if(result['type']=='list'):
    for item in result['data']:
        main(json_data=item,debug=False,safemode=False)
else:
    main(json_data=result,debug=False,safemode=False)