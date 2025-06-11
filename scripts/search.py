import sys
from trie import Trie

if __name__ == "__main__":
    word = "а+стра"
    trie = Trie()
    trie.json_load('dict/adv/trie.json')
    if len(sys.argv) > 1:
        word = sys.argv[1]
    print(trie.search(word))
