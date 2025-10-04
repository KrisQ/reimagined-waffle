from textnode import TextNode, TextType


def main():
    node = TextNode("dummy", TextType.LINK, "exampl.com")
    print(node)


if __name__ == "__main__":
    main()

