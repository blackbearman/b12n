import json
import pickle


def common_part(str1, str2):
    j = 1
    m = min(len(str1), len(str2))
    while j <= m and str1[-j] == str2[-j]:
        j += 1
    return j - 1


class RadixTree:
    def __init__(self):
        self.root = {}

    def insert(self, word, value):
        key = '$' + word
        node = self.root
        i = len(key) - 1
        while i >= 0:
            found_child = False
            for child_suffix, child_node in node.items():
                if key[i] == child_suffix[-1]:
                    found_child = True
                    j = common_part(key[:(i+1)], child_suffix)
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
                new_suffix = key[:(i+1)]
                node[new_suffix] = value
                break

    def search(self, word):
        key = '$' + word
        node = self.root
        i = len(key) - 1
        while i >= 0:
            found_child = False
            for child_suffix, child_node in node.items():
                if key[i] == child_suffix[-1]:
                    found_child = True
                    j = common_part(key[:(i+1)], child_suffix)
                    if j == len(child_suffix):
                        node = child_node
                    else:
                        return None
                    i -= j
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

    def dump(self, filename):
        with open(filename, 'wb') as fp:
            pickle.dump(self.root, fp)

    def load(self, filename):
        with open(filename, 'rb') as fp:
            self.root = pickle.load(fp)


if __name__ == "__main__":
    trie = RadixTree()
    trie.insert("фіяле+тава-сі+ні", "n")
    print(trie.root)
    trie.insert("барво+ва-сі+ні", "n")
    print(trie.root)
    trie.insert("ружо+ва-сі+ні", "n")
    print(trie.root)
    trie.insert("васілько+ва-сі+ні", "n")
    print(trie.root)
    trie.insert("сі+ні", "n")
    print(trie.root)
    print(trie.search("сі+ні"))
