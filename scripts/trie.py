import json


class Trie:
    def __init__(self) -> object:
        self.root = {}

    def insert(self, key, value):
        node = self.root
        i = len(key)-1
        while i >= 0:
            if key[i] not in node:
                node[key[i]] = {}
            node = node[key[i]]
            i -= 1
        node["$"] = value

    def search(self, key):
        node = self.root
        i = len(key) - 1
        while i >= 0:
            if key[i] not in node:
                return None
            node = node[key[i]]
            i -= 1
        return node["$"]

    def json_dump(self, filename):
        with open(filename, 'w', encoding="utf-8") as fp:
            json.dump(self.root, fp, ensure_ascii=False)

    def json_load(self, filename):
        with open(filename, 'r', encoding="utf-8") as fp:
            self.root = json.load(fp)

    def write_node(self, node, fp):
        fp.write("{")
        for key, item in node.items():
            fp.write(key)
            fp.write(":")
            if key == "$":
                fp.write(item)
            else:
                self.write_node(item, fp)
            fp.write(",")
        fp.write("}")

    def text_dump(self, filename):
        with open(filename, 'w', encoding='utf8') as fp:
            self.write_node(self.root, fp)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("astra", "n")
    trie.insert("fastra", "n")
    print(trie.root)
    print(trie.search("astra"))
