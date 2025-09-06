import unittest

from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_with_nested_parents(self):
        grandchild_node = LeafNode("b", "grandchild")
        grandchild2_node = LeafNode("b", "grandchild2")
        child_node = ParentNode("span", [grandchild_node, grandchild2_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b><b>grandchild2</b></span></div>",
        )

    def test_to_html_parent_with_props(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node], {"href": "https://www.boot.dev"})
        self.assertEqual(
            parent_node.to_html(),
            '<div href="https://www.boot.dev"><span><b>grandchild</b></span></div>'
        )

    def test_to_html_child_with_props(self):
        child_node = LeafNode("b", "child", {"href": "https://www.boot.dev"})
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            '<div><b href="https://www.boot.dev">child</b></div>'
        )
