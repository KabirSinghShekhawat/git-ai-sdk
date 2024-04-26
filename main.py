import ollama
from src.core.client import APIClient
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


modelfile = """
FROM llama3
PARAMETER temperature 1
SYSTEM You are an API calling tool. You only return code and JSON.
You don't return language, only Code or JSON.
You generate the functions and required data models and nothing else.
Always return json response and never call print() in the code.
"""

ollama.create(model="git", modelfile=modelfile)
api_client = APIClient(model='git')


response: dict = api_client.get_repo_info("KabirSinghShekhawat", "OIJPCR-front-end")
print(response.get('id', 'ID not present'))
user = api_client.get_user_info(response.get('owner', {}).get('login', ''))
print(user.keys())
