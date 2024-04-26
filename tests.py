import unittest

from src.core.client import APIClient


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


if __name__ == "__main__":
    unittest.main(verbosity=2)
