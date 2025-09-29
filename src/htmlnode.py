class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        if self.tag is None:
            return self.value or ""

        attrs = ""
        if self.props:
            attrs = " " + " ".join(f'{k}="{v}"' for k,v in self.props.items())

        if self.children:
            inner = "".join(child.to_html() for child in self.children)
            return f"<{self.tag}{attrs}>{inner}</{self.tag}>"

        inner = self.value or ""
        return f"<{self.tag}{attrs}>{inner}</{self.tag}>"


    def props_to_html(self):
        if not self.props:
            return ""
        parts = [f'{k}="{self.props[k]}"' for k in sorted(self.props)]
        return " " + " ".join(parts)

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag, self.value, self.children, self.props) == (other.tag, other.value, other.children, other.props)

    def __repr__(self):
        return f"HTMLNODE({self.tag}, {self.value}, {self.children}, {self.props})"
