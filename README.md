# GitHub API Client (Powered by Llama3)

## Features
- Fetch repository info.
- Fetch user info.

## Usage

1. Install Ollama and Llama3.
2. Create a python virtual env and install the requirements.
3. run `python main.py` to create the git model.
4. run `python tests.py` to run all the tests.

## Demo

In this demo, we can see that running the code generator LLM
for the same tests ran successfully before but fails for
one test case when ran again. This is because of code 
generation variance and hallucinations.

In this case, the LLM generated and ran the get all users route
instead of get user by username route.


https://github.com/KabirSinghShekhawat/git-ai-sdk/assets/51289863/e663c3a4-535f-4804-9c89-0be0caec60ca

## Architecture

<img width="1160" alt="Github API" src="https://github.com/KabirSinghShekhawat/git-ai-sdk/assets/51289863/c7c493f1-a2e4-420b-9c0d-96417f594a4d">


