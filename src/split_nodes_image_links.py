from textnode import TextNode, TextType
from extract_markdown_text_and_image import (
    extract_markdown_images,
    extract_markdown_links,
)


def split_nodes_image(old_nodes: list[TextNode]):
    text_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            text_nodes.append(node)
        else:
            images = extract_markdown_images(node.text)
            if len(node.text) == 0:
                pass
            elif len(images) == 0:
                text_nodes.append(node)
            else:
                remaining_text = node.text
                for description, url in images:
                    markdown_delimiter = f"![{description}]({url})"
                    part, remaining_text = remaining_text.split(markdown_delimiter, 1)
                    if len(part) > 0:
                        text_nodes.append(
                            TextNode(
                                part,
                                TextType.PLAIN,
                                None,
                            )
                        )
                    text_nodes.append(TextNode(description, TextType.IMAGE, url))
                if len(remaining_text) > 0:
                    text_nodes.append(TextNode(remaining_text, TextType.PLAIN, None))

    return text_nodes


def split_nodes_link(old_nodes: list[TextNode]):
    text_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.PLAIN:
            text_nodes.append(node)
        else:
            links = extract_markdown_links(node.text)
            if len(node.text) == 0:
                pass
            elif len(links) == 0:
                text_nodes.append(node)
            else:
                remaining_text = node.text
                for description, url in links:
                    markdown_delimiter = f"[{description}]({url})"
                    part, remaining_text = remaining_text.split(markdown_delimiter, 1)
                    if len(part) > 0:
                        text_nodes.append(
                            TextNode(
                                part,
                                TextType.PLAIN,
                                None,
                            )
                        )
                    text_nodes.append(TextNode(description, TextType.LINK, url))
                if len(remaining_text) > 0:
                    text_nodes.append(TextNode(remaining_text, TextType.PLAIN, None))
    return text_nodes
