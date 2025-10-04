class HTMLNode:
    def __init__(
        self,
        tag: str | None = None,
        value: str | None = None,
        children: list["HTMLNode"] | None = None,
        props: dict[str, str] | None = None,
    ) -> None:
        self.tag = tag
        self.value = value
        self.children = children
        # props e.g. link (<a> tag) might have {"href": "https://www.google.com"}
        self.props = props

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.props}, {self.value}, {self.children})"

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self) -> str:
        if self.props is None:
            return ""
        props_string = ""
        for key, value in self.props.items():
            props_string += f' {key}="{value}"'
        return props_string
