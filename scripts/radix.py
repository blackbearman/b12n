import json


class RadixTree:
    def __init__(self):
        self.root = {}

    def insert(self, key, value):
        node = self.root
        i = len(key) - 1
        while i > 0:
            found_child = False
            for child_suffix, child_node in node.items():
                if key[i] == child_suffix[-1]:
                    found_child = True
                    j = 1
                    m = min(len(child_suffix), i + 1)
                    while j <= m and key[i - j + 1] == child_suffix[-j]:
                        j += 1
                    j -= 1
                    if j == len(child_suffix):
                        node = child_node
                    else:
                        new_node = {child_suffix[:-j]: child_node}
                        del node[child_suffix]
                        node[child_suffix[-j:]] = new_node
                        node = new_node
                    i -= j
                    break
            if not found_child:
                new_suffix = '$' + key[:(i+1)]
                node[new_suffix] = value
                break

    def search(self, word):
        key = '$' + word
        node = self.root
        i = len(key)
        while i > 0:
            found_child = False
            for child_suffix, child_node in node.items():
                if key[i - len(child_suffix):i] == child_suffix:
                    node = child_node
                    i -= len(child_suffix)
                    found_child = True
                    break
            if not found_child:
                return None
        return node

    def json_dump(self, filename):
        with open(filename, 'w', encoding="utf-8") as fp:
            json.dump(self.root, fp, ensure_ascii=False)

    def json_load(self, filename):
        with open(filename, 'r', encoding="utf-8") as fp:
            self.root = json.load(fp)


if __name__ == "__main__":
    trie = RadixTree()
    trie.insert("astra", "n")
    print(trie.root)
    trie.insert("fastra", "n")
    print(trie.root)
    trie.insert("tra", "n")
    print(trie.root)
    trie.insert("sestra", "n")
    print(trie.root)
    trie.insert("sistra", "n")
    print(trie.root)
    print(trie.search("astra"))
