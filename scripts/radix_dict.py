import os

from xml.etree.ElementTree import parse

from radix import RadixTree

if __name__ == "__main__":
    trie = RadixTree()

    files = os.listdir("dict")
    for file in files:
        if file.endswith(".xml"):
            name = os.path.join("dict", file)
            print(name)
            tree = parse(name)
            root = tree.getroot()
            for paradigm in root:
                if paradigm.tag == "Paradigm":
                    for variant in paradigm:
                        if variant.tag == "Variant":
                            for form in variant:
                                if form.tag == "Form":
                                    trie.insert(form.text, file[0])

    trie.json_dump('dict/adv/radix.json')
