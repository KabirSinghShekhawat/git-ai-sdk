import unittest

from dotenv import load_dotenv

from src.core.client import APIClient

load_dotenv()  # take environment variables from .env.


class TestAPIClient(unittest.TestCase):
    def setUp(self):
        self.api_client = APIClient(model="git")

    def test_get_repo_info(self):
        repo_info = self.api_client.get_repo_info(
            "KabirSinghShekhawat", "OIJPCR-front-end"
        )
        self.assertEqual(
            repo_info.get("id", ""),
            427657339,
        )

    def test_get_user(self):
        user = self.api_client.get_user_info("KabirSinghShekhawat")
        self.assertEqual(user.get("id", ""), 51289863)

    def test_get_org_repos(self):
        repos = self.api_client.get_org_repos(
            "stackithq", "private", "created_at", "desc", 10
        )
        self.assertEqual(len(repos), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
