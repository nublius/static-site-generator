import unittest

from leafnode import LeafNode

class TestLeafNode(unittest.TestCase):
    def test_eq(self):
        node = LeafNode('p', 'Yep')
        node2 = LeafNode('p', 'Yep')
        self.assertEqual(node, node2)

    def test_eq2(self):
        node = LeafNode('div', 'Yep')
        node2 = LeafNode('p', 'Yep')
        self.assertNotEqual(node, node2)

    def test_eq3(self):
        node = LeafNode('p', 'This is a test', {"href": "https://www.boot.dev", "src": "/img/cat.png"})
        node2 = LeafNode('p', 'This is a test', {"src": "/img/cat.png", "href": "https://www.boot.dev"})
        self.assertEqual(node, node2)

    def test_eq4(self):
        node = LeafNode('div', 'This is a test', {"href": "https://www.boot.dev", "src": "/img/cat.png"})
        node2 = LeafNode('p', 'This is a test', {"src": "/img/cat.png", "href": "https://www.boot.dev"})
        self.assertNotEqual(node, node2)


