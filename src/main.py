from textnode import TextNode, TextType

def main():
    dummy = TextNode('Anchor text', TextType.LINK, 'https://www.boot.dev')

    print(dummy)

if __name__ == "__main__":
    main()
