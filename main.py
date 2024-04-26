import os

import ollama
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import HumanMessagePromptTemplate
from langchain.prompts.chat import ChatPromptTemplate
from langchain_community.chat_models import ChatOllama

from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()  # take environment variables from .env.


class CodeParse(BaseModel):
    code: str = Field(description="The python code for making API requests to github.")


modelfile = """
FROM llama3
SYSTEM You are a 3rd party SaaS integration code generator. You only generate code and nothing else.
You generate the functions and required data models and nothing else.
Always return json response and never call print() in the code.
"""

PROMPT = """
    Write python code for making a get user request to {platform}."
    {format_instructions} 
"""
ollama.create(model="git", modelfile=modelfile)


def demo():
    llm = ChatOllama(model="git")
    # Set up a parser + inject instructions into the prompt template.
    parser = PydanticOutputParser(pydantic_object=CodeParse)

    # setup the chat model
    message = HumanMessagePromptTemplate.from_template(
        template=PROMPT,
    )
    chat_prompt = ChatPromptTemplate.from_messages([message])

    # get user input
    platform_name = input("Platform(GitHub/GitLab): ")

    # generate the response
    print("Generating response...")
    chat_prompt_with_values = chat_prompt.format_prompt(
        platform=platform_name, format_instructions=parser.get_format_instructions()
    )
    output = llm(chat_prompt_with_values.to_messages())
    code = parser.parse(output.content)
    print(code)


#
# github_secret = os.environ.get("GITHUB_API_KEY", "")
# output = ollama.generate(
# model="git", prompt="Write python code for making a get user request to github."
# )
# print(output)

if __name__ == "__main__":
    demo()
