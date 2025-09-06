from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value == None:
            raise ValueError("LeafNode must have a value")
        if self.tag == None:
            return self.value
        if self.props == None:
            return (f"<{self.tag}>{self.value}</{self.tag}>")
        else:
            html_props = super().props_to_html()
            return (f"<{self.tag}{html_props}>{self.value}</{self.tag}>")

