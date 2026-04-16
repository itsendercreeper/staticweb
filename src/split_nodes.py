import re
from textnode import TextNode, TextType
from extract_markdown import extract_markdown_images, extract_markdown_links

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_images(text)
        if not matches:
            new_nodes.append(node)
            continue

        pattern = r"!

\[([^\]

]+)\]

\(([^)]+)\)"
        parts = re.split(pattern, text)

        i = 0
        while i < len(parts):
            if i % 3 == 0:
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                alt = parts[i]
                url = parts[i + 1]
                new_nodes.append(TextNode(alt, TextType.IMAGE, url))
                i += 1
            i += 1

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        text = node.text
        matches = extract_markdown_links(text)
        if not matches:
            new_nodes.append(node)
            continue

        pattern = r"

\[([^\]

]+)\]

\(([^)]+)\)"
        parts = re.split(pattern, text)

        i = 0
        while i < len(parts):
            if i % 3 == 0:
                if parts[i]:
                    new_nodes.append(TextNode(parts[i], TextType.TEXT))
            else:
                anchor = parts[i]
                url = parts[i + 1]
                new_nodes.append(TextNode(anchor, TextType.LINK, url))
                i += 1
            i += 1

    return new_nodes
