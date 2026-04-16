import unittest
from parentnode import ParentNode
from leafnode import LeafNode

class TestParentNode(unittest.TestCase):

    def test_to_html_with_children(self):
        child = LeafNode("span", "child")
        parent = ParentNode("div", [child])
        self.assertEqual(parent.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild = LeafNode("b", "grandchild")
        child = ParentNode("span", [grandchild])
        parent = ParentNode("div", [child])
        self.assertEqual(
            parent.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_multiple_children(self):
        children = [
            LeafNode("b", "Bold"),
            LeafNode(None, " text "),
            LeafNode("i", "italic"),
        ]
        parent = ParentNode("p", children)
        self.assertEqual(
            parent.to_html(),
            "<p><b>Bold</b> text <i>italic</i></p>",
        )

    def test_missing_tag_raises(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [])

    def test_missing_children_raises(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None)

    def test_empty_children_list(self):
        # Empty list is allowed — it should render with no inner HTML
        parent = ParentNode("div", [])
        self.assertEqual(parent.to_html(), "<div></div>")

    def test_props_render_correctly(self):
        child = LeafNode(None, "text")
        parent = ParentNode("p", [child], props={"class": "main", "id": "x"})
        self.assertEqual(
            parent.to_html(),
            '<p class="main" id="x">text</p>',
        )

    def test_nested_mixed_nodes(self):
        parent = ParentNode(
            "section",
            [
                LeafNode("h1", "Title"),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "inside"),
                        LeafNode("b", "bold"),
                    ],
                ),
            ],
        )
        self.assertEqual(
            parent.to_html(),
            "<section><h1>Title</h1><div>inside<b>bold</b></div></section>",
        )
