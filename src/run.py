import os
import pathlib
import subprocess

from genericpath import exists

from src.data_processing.parse import extract_code_block
from src.data_processing.post_processing import DataProcessor


class CodeRunner:
    def __init__(self, env_map: dict[str, str]) -> None:
        os.environ.update(env_map)

    def run(self, llm_output: str):
        code_block = extract_code_block(llm_output)
        try:
            output = self.execute_command_and_return_output(code_block)
            output_json = DataProcessor(model="stripe", data=output).to_json()
            return output_json
        except Exception as e:
            print(f"Error evaluating code: {e}")

    def execute_command_and_return_output(self, command):
        cwd = pathlib.Path(__file__).parent
        temp_file_path = cwd / "temp.py"
        try:
            with open(temp_file_path, "w+") as f:
                f.write(command)
        except Exception as err:
            print(err)
            raise err

        def cleanup():
            try:
                if exists(temp_file_path):
                    os.remove(temp_file_path)
                else:
                    print(f"{temp_file_path} does not exist")
            except Exception as e:
                print(e)
                raise e

        process = subprocess.Popen(
            ["python", temp_file_path],
            cwd=cwd,
            stdout=subprocess.PIPE,
            stderr=open(cwd / "error.log", "w"),
        )
        output, error = process.communicate()
        cleanup()
        if error:
            raise Exception(str(error.decode()))
        return output.decode()
