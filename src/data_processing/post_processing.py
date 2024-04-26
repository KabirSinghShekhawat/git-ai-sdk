import json

from src.utils import generate_random_filename


def correctSingleQuoteJSON(s):
    rstr = ""
    escaped = False

    for c in s:

        if c == "'" and not escaped:
            c = '"'  # replace single with double quote

        elif c == "'" and escaped:
            rstr = rstr[:-1]  # remove escape character before single quotes

        elif c == '"':
            c = "\\" + c  # escape existing double quotes

        escaped = c == "\\"  # check for an escape character
        rstr += c  # append the correct json

    return rstr


class DataProcessor:
    def __init__(self, model: str = "llama3", data: str = "[]") -> None:
        self.model = model
        self.data = data

    def to_json(self) -> str:
        output = correctSingleQuoteJSON(self.data)
        output = output.replace("None", "null")
        output = output.replace("False", "false").replace("True", "true")

        with open(f"{generate_random_filename()}.json", "w+") as f:
            f.write(output)

        return output

    def to_dict(self) -> dict:
        try:
            output_json = self.to_json()
            response = json.loads(output_json)
            return response
        except Exception as err:
            print("DataProcessor `to_dict()` failed to parse output")
            print(err)
