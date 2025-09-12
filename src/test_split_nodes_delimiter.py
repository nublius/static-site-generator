import unittest

from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter

class TestSplit(unittest.TestCase):
    def test_bold(self):
        node = TextNode("This is text with a **bold block** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        comparison = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold block", TextType.BOLD),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, comparison)

    def test_multiple_bold(self):
        node = TextNode("This is text with **multiple bold blocks** inside **it**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        comparison = [
            TextNode("This is text with ", TextType.TEXT),
            TextNode("multiple bold blocks", TextType.BOLD),
            TextNode(" inside ", TextType.TEXT),
            TextNode("it", TextType.BOLD),
        ]
        self.assertEqual(new_nodes, comparison)

    def test_italic(self):
        node = TextNode("This is text with a _italic block_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        comparison = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("italic block", TextType.ITALIC),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, comparison)



    def test_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        comparison = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        self.assertEqual(new_nodes, comparison)

    def test_no_match(self):
        node = TextNode("This is text with no `match", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)


        
