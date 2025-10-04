import unittest
from markdown_to_blocks import markdown_to_blocks
from block_to_blocktype import block_to_block_type
from blocktype import BlockType


class TestMdToBl(unittest.TestCase):
    def test_markdown_to_blocks(self):
        md = """
            This is **bolded** paragraph

            This is another paragraph with _italic_ text and `code` here
            This is the same paragraph on a new line

            - This is a list
            - with items
            """
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_block_to_blocktype(self):
        h_block = "# Heading 1"
        self.assertEqual(block_to_block_type(h_block), BlockType.HEADING)

        h_block2 = "### Heading 3"
        self.assertEqual(block_to_block_type(h_block2), BlockType.HEADING)

        code_block = "```\ncode here\n```"
        self.assertEqual(block_to_block_type(code_block), BlockType.CODE)

        quote_block = "> This is a quote\n> Another line"
        self.assertEqual(block_to_block_type(quote_block), BlockType.QUOTE)

        ul_block2 = "- Item 1\n- Item 2"
        self.assertEqual(block_to_block_type(ul_block2), BlockType.UNORDERED_LIST)

        ol_block = "1. First item\n2. Second item\n3. Third item"
        self.assertEqual(block_to_block_type(ol_block), BlockType.ORDERED_LIST)

        p_block = "Just a regular paragraph"
        self.assertEqual(block_to_block_type(p_block), BlockType.PARAGRAPH)
