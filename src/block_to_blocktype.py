from blocktype import BlockType


def is_x_block(block, delimiter):
    lines = block.split("\n")
    for line in lines:
        if not line.startswith(delimiter):
            return False
    return True


def is_ordered_list(block):
    lines = block.split("\n")
    num = 1
    for line in lines:
        if not line:
            return False

        i = 0
        while i < len(line) and line[i].isdigit():
            i += 1

        if i == 0 or not line[i:].startswith(". "):
            return False

        line_num = int(line[:i])
        if line_num != num:
            return False

        num += 1

    return True


def starts_with_ordered_list(line):
    return line and line[0].isdigit() and ". " in line


def block_to_block_type(block):
    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    elif block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    elif is_x_block(block, ">"):
        return BlockType.QUOTE
    elif is_x_block(block, "- "):
        return BlockType.UNORDERED_LIST
    elif is_ordered_list(block):
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH
