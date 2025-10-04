from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        if not value:
            raise ValueError("Missing value")

        super().__init__(tag, value, None, props)

        if self.children is not None:
            raise ValueError("children must be none")

    def __repr__(self) -> str:
        return f"LeafNode({self.tag}, {self.props}, {self.value})"

    def to_html(self):
        if not self.value:
            raise ValueError("Missing value")
        if not self.tag:
            return self.value
        return f"<{self.tag}{self.props_to_html() if self.props else ''}>{self.value}</{self.tag}>"
