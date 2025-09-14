from textnode import TextType, TextNode
from split_nodes_delimiter import split_nodes_delimiter
from split_nodes_images_and_link import split_nodes_image, split_nodes_link

def text_to_textnodes(text):
    node = TextNode(text, TextType.TEXT)
    code_check = split_nodes_delimiter([node], "`", TextType.CODE)
    bold_check = split_nodes_delimiter(code_check, "**", TextType.BOLD)
    italic_check = split_nodes_delimiter(bold_check, "_", TextType.ITALIC)
    image_check = split_nodes_image(italic_check)
    link_check = split_nodes_link(image_check)

    return link_check

