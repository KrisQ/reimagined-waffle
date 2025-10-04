from htmlnode import HTMLNode


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: list["HTMLNode"],
        props: dict[str, str] | None = None,
    ) -> None:
        if not tag:
            raise ValueError("Missing tag")
        if not children:
            raise ValueError("Missing children")

        super().__init__(tag, None, children, props)

        if self.value is not None:
            raise ValueError("Value must be none")

    def __repr__(self) -> str:
        return f"ParentNode({self.tag}, {self.props}, {self.value})"

    def to_html(self):
        if not self.children:
            raise ValueError("Missing children")
        if not self.tag:
            raise ValueError("Missing tag")

        return f"<{self.tag}{self.props_to_html() if self.props else ''}>{''.join(c.to_html() for c in self.children)}</{self.tag}>"
