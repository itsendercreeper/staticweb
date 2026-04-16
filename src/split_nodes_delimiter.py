from textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        # Only split plain text nodes
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        parts = node.text.split(delimiter)

        # If we have an odd number of parts, delimiters are unbalanced
        if len(parts) % 2 == 0:
            raise Exception(f"Unmatched delimiter '{delimiter}' in text: {node.text}")

        # Rebuild nodes
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # Even index → normal text
                if part:
                    new_nodes.append(TextNode(part, TextType.TEXT))
            else:
                # Odd index → inside delimiters → special type
                if part:
                    new_nodes.append(TextNode(part, text_type))

    return new_nodes
