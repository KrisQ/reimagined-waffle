import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_repr_with_all_attributes(self):
        """Test repr with all attributes set"""
        node = HTMLNode(
            "a", "val test", None, {"href": "example.com", "data-rand": "092483"}
        )
        expected = "HTMLNode(a, {'href': 'example.com', 'data-rand': '092483'}, val test, None)"
        self.assertEqual(repr(node), expected)

    def test_repr_with_only_tag(self):
        """Test repr with only tag set"""
        node = HTMLNode("div", None, None, None)
        expected = "HTMLNode(div, None, None, None)"
        self.assertEqual(repr(node), expected)

    def test_repr_with_tag_and_value(self):
        """Test repr with tag and value"""
        node = HTMLNode("p", "Hello World", None, None)
        expected = "HTMLNode(p, None, Hello World, None)"
        self.assertEqual(repr(node), expected)

    def test_repr_with_tag_and_props(self):
        """Test repr with tag and props"""
        node = HTMLNode("img", None, None, {"src": "image.png", "alt": "test"})
        expected = "HTMLNode(img, {'src': 'image.png', 'alt': 'test'}, None, None)"
        self.assertEqual(repr(node), expected)


if __name__ == "__main__":
    unittest.main()
