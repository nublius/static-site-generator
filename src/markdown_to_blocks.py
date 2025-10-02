def markdown_to_blocks(text):
    blocks = []
    current = []
    in_code = False

    def flush():
        nonlocal current
        if current:
            blocks.append("\n".join(current).strip())
            current = []

    for line in text.splitlines():
        if in_code:
            current.append(line)
            if line.lstrip().startswith("```"):
                in_code = False
                flush()
            continue

        if line.strip() == "":
            flush()
            continue

        if line.lstrip().startswith("```"):
            flush()
            in_code = True
            current.append(line)
            continue

        if line.lstrip().startswith("#"):
            flush()
            blocks.append(line.strip())
            continue

        current.append(line)

    flush()
    return blocks
#    blocks = text.split("\n\n")
#    return [b.strip() for b in blocks if b.strip()]

