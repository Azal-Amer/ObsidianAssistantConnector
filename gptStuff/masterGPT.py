import json
import os
from openai import OpenAI
from dotenv import load_dotenv
from gptStuff.parent import parent
from gptStuff.sister import sister
from gptStuff.brother import brother

load_dotenv()
prompt = "Remember that Ananya loves to crochet"
def GPTFlow(prompt):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    # get the api key from the environment
    model_engine = "text-davinci-002"  # Specify the GPT-3.5 model engine
    max_tokens = 50  # Adjust the maximum number of tokens in the response
    temperature = 0.7  # Adjust the creativity of the response (0.0 to 1.0)
    client = OpenAI(
        # This is the default and can be omitted
        api_key=openai_api_key,
    )
    controlPrompt = parent(prompt,client)
    brotherData = sister(controlPrompt,client)
    return brother(brotherData,controlPrompt,client)