import unittest
from textnode import TextNode, TextType
from textnode_to_htmlnode import text_node_to_html_node
from leafnode import LeafNode

class TestTextNodeToHTMLNode(unittest.TestCase):

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, None)
        self.assertEqual(html.value, "This is a text node")

    def test_bold(self):
        node = TextNode("Bold", TextType.BOLD)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "b")
        self.assertEqual(html.value, "Bold")

    def test_italic(self):
        node = TextNode("Italic", TextType.ITALIC)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "i")
        self.assertEqual(html.value, "Italic")

    def test_code(self):
        node = TextNode("print('hi')", TextType.CODE)
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "code")
        self.assertEqual(html.value, "print('hi')")

    def test_link(self):
        node = TextNode("Boot.dev", TextType.LINK, "https://www.boot.dev")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "a")
        self.assertEqual(html.value, "Boot.dev")
        self.assertEqual(html.props, {"href": "https://www.boot.dev"})

    def test_image(self):
        node = TextNode("alt text", TextType.IMAGE, "https://img.com/x.png")
        html = text_node_to_html_node(node)
        self.assertEqual(html.tag, "img")
        self.assertEqual(html.value, "")
        self.assertEqual(html.props, {
            "src": "https://img.com/x.png",
            "alt": "alt text",
        })

    def test_invalid_type(self):
        node = TextNode("text", "not-a-valid-type")
        with self.assertRaises(Exception):
            text_node_to_html_node(node)
