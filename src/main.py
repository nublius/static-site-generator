from textnode import TextNode, TextType
from htmlnode import HTMLNode

def main():
    textnode = TextNode('Anchor text', TextType.LINK, 'https://www.boot.dev')

    htmlnode = HTMLNode('p', 'Hello world!', None, {"href": "https://www.boot.dev"})

    print(textnode)

    print(htmlnode)

    print(htmlnode.props_to_html())

if __name__ == "__main__":
    main()
