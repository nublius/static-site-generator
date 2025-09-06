import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode('p', 'This is a test.', ['child'])
        node2 = HTMLNode('p', 'This is a test.', ['child'])
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = HTMLNode('div', 'This is a test.')
        node2 = HTMLNode('p', 'This is a test.')
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = HTMLNode('p', 'This is a test', None, {"href": "https://www.boot.dev", "src": "/img/cat.png"})
        node2 = HTMLNode('p', 'This is a test', None, {"src": "/img/cat.png", "href": "https://www.boot.dev"})
        self.assertEqual(node, node2)


