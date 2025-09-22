import unittest
from blocktype import BlockType, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_paragraph(self):
        block = "This is a paragraph"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block)) 

    def test_code(self):
        block = "``` code block ```"
        self.assertEqual(BlockType.CODE, block_to_block_type(block))

    def test_quote(self):
        block = "> Hello\n>Quote\n>Yep"
        self.assertEqual(BlockType.QUOTE, block_to_block_type(block))

    def test_quote2(self):
        block = ">Not a quote\nI repeat\n>Not a quote"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_unordered_list(self):
        block = "- One\n- Two\n- Three"
        self.assertEqual(BlockType.UNORDERED_LIST, block_to_block_type(block))

    def test_ordered_list(self):
        block = "1. Milk\n2. Yogurt\n3. Beef"
        self.assertEqual(BlockType.ORDERED_LIST, block_to_block_type(block))

    def test_ordered_list2(self):
        block = "1. Milk\n3. Yogurt"
        self.assertEqual(BlockType.PARAGRAPH, block_to_block_type(block))

    def test_heading(self):
        block = "# Heading"
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))

    def test_heading2(self):
        block = "## Heading"
        self.assertEqual(BlockType.HEADING, block_to_block_type(block))
