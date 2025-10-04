import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_repr(self):
        node = TextNode("test", TextType.ITALIC, "example.com")
        self.assertEqual(repr(node), "TextNode(test, italic, example.com)")

    def test_enum(self):
        self.assertNotEqual(TextType.BOLD, "Bold")
        self.assertNotEqual(TextType.ITALIC, "italic")

    def wrong_texttype(self):
        with self.assertRaises(Exception):
            TextNode("test", "hello")

    def test_url(self):
        node = TextNode("test", TextType.LINK, "example.com")
        self.assertEqual(node.url, "example.com")


if __name__ == "__main__":
    unittest.main()
