def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    results = []
    for block in blocks:
        if block.strip() != "":
            if "\n" not in block:
                results.append(block.strip())
            else:
                lines = block.strip().split("\n")
                stripped_results = []
                for line in lines:
                    if line.strip() != "":
                        stripped_results.append(line.strip())
                results.append("\n".join(stripped_results))

    return results
