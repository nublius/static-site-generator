from textnode import TextType, TextNode
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        else:
            new_parts = []
            images = extract_markdown_images(old_node.text)
            if not images:
                new_nodes.append(old_node)
                continue
            else:
                # For each image tuple found
                sections = old_node.text.split(f"![{images[0][0]}]({images[0][1]})", 1)
                # If sections[0] is not empty, make text node
                if sections[0]:
                    new_parts.append(TextNode(sections[0], TextType.TEXT))

                # Handle image itself
                new_parts.append(TextNode(images[0][0], TextType.IMAGE, images[0][1]))

                # Recursively find other images
                if sections[1]:
                    remaining_node = TextNode(sections[1], TextType.TEXT)
                    remaining_parts = split_nodes_image([remaining_node])
                    new_parts.extend(remaining_parts)

        new_nodes.extend(new_parts)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT:
            new_nodes.append(old_node)
            continue
        
        else:
            new_parts = []
            links = extract_markdown_links(old_node.text)
            if not links:
                new_nodes.append(old_node)
                continue
            else:
                # For each image tuple found
                sections = old_node.text.split(f"[{links[0][0]}]({links[0][1]})", 1)
                # If sections[0] is not empty, make text node
                if sections[0]:
                    new_parts.append(TextNode(sections[0], TextType.TEXT))

                # Handle image itself
                new_parts.append(TextNode(links[0][0], TextType.LINK, links[0][1]))

                # Recursively find other images
                if sections[1]:
                    remaining_node = TextNode(sections[1], TextType.TEXT)
                    remaining_parts = split_nodes_link([remaining_node])
                    new_parts.extend(remaining_parts)

        new_nodes.extend(new_parts)
    return new_nodes

