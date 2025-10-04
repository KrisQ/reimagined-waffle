from split_node_delimiter import split_nodes_delimiter
from split_nodes_image_links import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


def text_to_textnode(text):
    nodes = [TextNode(text, TextType.PLAIN, None)]
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return [n for n in nodes if not (n.text_type == TextType.PLAIN and n.text == "")]
