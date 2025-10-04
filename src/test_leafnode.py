from leafnode import LeafNode
import unittest


class TestTextNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")
        node2 = LeafNode("a", "home", {"href": "/home", "id": "1"})
        self.assertEqual(node2.to_html(), '<a href="/home" id="1">home</a>')
