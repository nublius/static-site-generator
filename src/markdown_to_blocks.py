def markdown_to_blocks(text):
    blocks = text.split("\n\n")
    return [b.strip() for b in blocks if b.strip()]

