import unittest
from main import extract_title


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        markdown = """
            test
            # Welcome y'all
            Bienvenu!
        """
        self.assertEqual(extract_title(markdown), "Welcome y'all")
