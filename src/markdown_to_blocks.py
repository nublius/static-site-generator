def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    for block in blocks:
        block = block.strip()

    complete_blocks = []
    for block in blocks:
        if block:
            complete_blocks.append(block)

    return complete_blocks

