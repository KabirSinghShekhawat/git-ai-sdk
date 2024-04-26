import ollama
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


modelfile = """
FROM llama3
PARAMETER temperature 0.8
SYSTEM You are an API calling tool. You only return code and JSON.
You don't return language, only Code or JSON.
You generate the functions and required data models and nothing else.
Always return json response and never call print() in the code.
"""

ollama.create(model="git", modelfile=modelfile)
