import re
ol_re = re.compile(r"^\d+\.\s")
def is_ul(line): return line.lstrip().startswith(("- ", "* "))
def is_ol(line): return bool(ol_re.match(line.lstrip()))

def markdown_to_blocks(text):
    blocks = []
    current = []
    current_kind = ""

    def flush():
        nonlocal current
        nonlocal current_kind
        if current:
            blocks.append("\n".join(current).strip())
            current = []
            current_kind = ""

    for line in text.splitlines():
        if current_kind == "code":
            current.append(line)
            if line.lstrip().startswith("```"):
                flush()
            continue

        if line.strip() == "":
            flush()
            continue

        if line.lstrip().startswith("```"):
            flush()
            current_kind = "code"
            current.append(line)
            continue

        if line.lstrip().startswith("#"):
            flush()
            blocks.append(line.strip())
            continue

        if is_ul(line):
            if current_kind != "ul":
                flush()
                current_kind = "ul"
            current.append(line)
            continue

        if is_ol(line):
            if current_kind != "ol":
                flush()
                current_kind = "ol"
            current.append(line)
            continue

        if current_kind != "para":
            flush()
            current_kind = "para"
        current.append(line)

    flush()

    return blocks
#    blocks = text.split("\n\n")
#    return [b.strip() for b in blocks if b.strip()]

