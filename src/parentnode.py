from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)

    def to_html(self):
        if self.tag == None:
            raise ValueError("ParentNode must have a tag")
        if self.children == None:
            raise ValueError("ParentNode must have children")
        
        inner = "".join(child.to_html() for child in self.children)
        if self.props is None:
            return (f"<{self.tag}>{inner}</{self.tag}>")
        else:
            return (f"<{self.tag}{self.props_to_html()}>{inner}</{self.tag}>")
