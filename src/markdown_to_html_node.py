from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from extract_markdown import extract_markdown_images, extract_markdown_links
from blocktype import BlockType, block_to_block_type
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

def markdown_to_html_node(markdown):
    split_markdown = markdown_to_blocks(markdown)
    for block in split_markdown:
        blocktype = block_to_block_type(block)
        

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]

