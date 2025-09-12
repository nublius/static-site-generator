from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type is not TextType.TEXT or old_node.text.count(delimiter) == 0:
            new_nodes.append(old_node)
            continue

        if (old_node.text.count(delimiter) % 2) != 0:
            raise Exception("Invalid markdown syntax")

        else:
            new_parts = []
            parts = old_node.text.split(delimiter)
            for i, chunk in enumerate(parts):
                if not chunk:
                    continue
                tt = text_type if (i % 2 == 1) else TextType.TEXT
                new_parts.append(TextNode(chunk, tt))

        new_nodes.extend(new_parts)

    return new_nodes




    

        
    
