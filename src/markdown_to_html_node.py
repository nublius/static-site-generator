import re
from htmlnode import HTMLNode
from markdown_to_blocks import markdown_to_blocks
from extract_markdown import extract_markdown_images, extract_markdown_links
from blocktype import BlockType, block_to_block_type
from text_node_to_html_node import text_node_to_html_node
from text_to_textnodes import text_to_textnodes

OL_MARKER = re.compile(r"^\d+\.\s")

def markdown_to_html_node(markdown):
    split_markdown = markdown_to_blocks(markdown)
    for block in split_markdown:
        blocktype = block_to_block_type(block)
        
def text_to_children(text):
    textnodes = text_to_textnodes(text)
    return [text_node_to_html_node(tn) for tn in textnodes]

def parse_heading(line):
    i = 0
    while i < len(line) and line[i] == "#":
        i += 1
    # i is count of '#'
    if i == 0 or i > 6:
        return None, line # not a heading
    if i < len(line) and line[i] == " ":
        return i, line[i + 1:]
    return None, line 

def parse_quote(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if line.startswith("> "):
            new_lines.append(line[2:])
        elif line.startswith(">"):
            new_lines.append(line[1:])
        else:
            new_lines.append(line)
    return "\n".join(new_lines)

def parse_unordered_list(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if line.startswith("- "):
            new_lines.append(line[2:])
        elif line.startswith("-"):
            new_lines.append(line[1:])
        else:
            new_lines.append(line)
    return new_lines

def parse_ordered_list(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if is_ordered_item(line):
            new_lines.append(strip_ordered_marker(line))
        else:
            new_lines.append(line)
    return new_lines

def is_ordered_item(line):
    return bool(OL_MARKER.match(line))

def strip_ordered_marker(line):
    return OL_MARKER.sub("", line, count=1)
