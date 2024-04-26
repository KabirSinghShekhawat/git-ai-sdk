from enum import Enum
import os
from src.run import CodeRunner
import ollama


class Platforms(Enum):
    GITHUB = "GitHub"
    GITLAB = "GitLab"


class APIClient:
    def __init__(self, model: str = "llama3", platform: Platforms = Platforms.GITHUB):
        self.model = model
        self.api_key_name = f"{platform.name}_API_KEY"
        self.api_key = os.environ.get(self.api_key_name, "")
        self.base_prompt = f"""The API key is in `os.environ.get({self.api_key_name})`.
        Only write code. Do not explain anything. Values for params will be provided.
        Add error handling code, return the response from API directly.
        Wrap all code in <code></code> blocks.
        """

    def get_repo_info(self, repo_owner: str, repo_name: str):
        """
        Get information about a repository.

        :param repo_owner: Owner of the repository.
        :param repo_name: Name of the repository.
        :return: JSON response containing repository information.
        """
        prompt = self.base_prompt + "Write python code to fetch a repo."
        prompt += f"repo_owner='{repo_owner}'|repo_name='{repo_name}'"
        return self.run_prompt(prompt)

    def get_user_info(self, username):
        """
        Get information about a user.

        :param username: GitHub username.
        :return: JSON response containing user information.
        """
        prompt = self.base_prompt + "Write python code to fetch a username."
        prompt += "use the values provided below in the format key='value'"
        prompt += f"username='{username}'"
        return self.run_prompt(prompt)

    def run_prompt(self, prompt: str):
        output = ollama.generate(
            model=self.model,
            prompt=prompt,
        )

        runner = CodeRunner(env_map={self.api_key_name: self.api_key}, model=self.model)
        response: dict = runner.run(output["response"])
        return response or {}
