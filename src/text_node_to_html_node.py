from leafnode import LeafNode
from htmlnode import HTMLNode
from textnode import TextNode, TextType


def text_node_to_html_node(text_node: TextNode) -> HTMLNode:
    match text_node.text_type:
        case TextType.PLAIN:
            return LeafNode(None, text_node.text, None)
        case TextType.BOLD:
            return LeafNode("b", text_node.text, None)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text, None)
        case TextType.CODE:
            return LeafNode("code", text_node.text, None)
        case TextType.LINK:
            return LeafNode(
                "a", text_node.text, {"href": text_node.url if text_node.url else ""}
            )
        case TextType.IMAGE:
            return LeafNode(
                "img", text_node.text, {"href": text_node.url if text_node.url else ""}
            )
