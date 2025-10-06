from enum import Enum
import re

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    if re.match(r"^#{1,6} ", block):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```") and len(block) >= 6:
        return BlockType.CODE
    else:
        lines = [ln for ln in block.split("\n") if ln.strip() != ""]
        if all(line.startswith(">") for line in lines):
            return BlockType.QUOTE
        elif all(line.lstrip().startswith(("- ", "* ")) for line in lines):
            return BlockType.UNORDERED_LIST
        else:
            nums = []
            for line in lines:
                m = re.match(r"^(\d+)\. ", line.lstrip())
                if m is None:
                    return BlockType.PARAGRAPH
                else:
                    num = int(m.group(1))
                    nums.append(num)
            if nums == list(range(1, len(lines)+1)):
                return BlockType.ORDERED_LIST
        return BlockType.PARAGRAPH

        
