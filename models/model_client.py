from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import os
load_dotenv()
api_key=os.getenv('GEMINI_API_KEY')

def get_model(api_key=api_key):
    model_client = OpenAIChatCompletionClient(
    model="gemini-2.0-flash",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
    api_key=api_key
)
    return model_client
