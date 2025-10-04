from textnode import TextNode, TextType


def split_nodes_delimiter(
    old_nodes: list[TextNode], delimiter: str, text_type: TextType
) -> list[TextNode]:
    text_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            text_nodes.append(node)
        elif node.text.count(delimiter) % 2 != 0:
            raise Exception("invalid markdown syntax")
        else:
            parts = node.text.split(delimiter)
            for i, part in enumerate(parts):
                if part:
                    if i % 2 == 0:
                        text_nodes.append(TextNode(part, TextType.PLAIN, None))
                    else:
                        text_nodes.append(TextNode(part, text_type, None))

    return text_nodes
