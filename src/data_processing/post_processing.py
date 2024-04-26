import json

import ollama


class DataProcessor:
    def __init__(self, model: str = "llama3", data: str = "[]") -> None:
        self.model = model
        self.data = data

    def to_json(self):
        prompt = f"Only return JSON no english. Generate a valid json string from this (fix single quotes to double): {self.data}"
        output = ollama.generate(model=self.model, prompt=prompt)
        response_json = json.loads(output['response'])
        return response_json
