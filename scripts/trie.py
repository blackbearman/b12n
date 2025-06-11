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
        with open(filename, 'w') as fp:
            json.dump(self.root, fp)

    def json_load(self, filename):
        with open(filename, 'r') as fp:
            self.root = json.load(fp)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("astra", "n")
    trie.insert("fastra", "n")
    print(trie.root)
    print(trie.search("astra"))
