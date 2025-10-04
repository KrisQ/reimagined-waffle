import unittest
from split_node_delimiter import split_nodes_delimiter
from textnode import TextNode, TextType


class TestSplitNode(unittest.TestCase):
    def test_text(self):
        starting_text = TextNode(
            "This is text with a **bolded phrase** in the middle", TextType.PLAIN
        )
        expected_result = [
            TextNode("This is text with a ", TextType.PLAIN),
            TextNode("bolded phrase", TextType.BOLD),
            TextNode(" in the middle", TextType.PLAIN),
        ]
        self.assertEqual(
            split_nodes_delimiter([starting_text], "**", TextType.BOLD), expected_result
        )
