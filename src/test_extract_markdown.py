import unittest

from extract_markdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def test_image(self):
        matches = extract_markdown_images(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
        )
        self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

    def test_multiple_image(self):
        matches = extract_markdown_images(
            "This is text with ![rickroll](https://i.imgur.com/rickroll.png) and ![yoda](https://i.imgur.com/yoda.png)"
        )
        self.assertListEqual([("rickroll", "https://i.imgur.com/rickroll.png"), ("yoda", "https://i.imgur.com/yoda.png")], matches)

    def test_link(self):
        matches = extract_markdown_links(
            "This is text with a [link](https://www.boot.dev)"
        )
        self.assertListEqual([("link", "https://www.boot.dev")], matches)

    def test_multiple_link(self):
        matches = extract_markdown_links(
            "This is text with a link to [youtube](https://www.youtube.com) and [bootdev](https://www.boot.dev)"
        )
        self.assertListEqual([("youtube", "https://www.youtube.com"), ("bootdev", "https://www.boot.dev")], matches)
