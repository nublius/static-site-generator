import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'This is a test.', ['child'])
        node2 = HTMLNode('p', 'This is a test.', ['child'])
        self.assertEqual(node, node2)

