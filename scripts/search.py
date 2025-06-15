import sys
from radix import RadixTree

if __name__ == "__main__":
    word = "а+стра"
    trie = RadixTree()
    trie.load('dict/adv/radix.pkl')
    if len(sys.argv) > 1:
        word = sys.argv[1]
    print(trie.search(word))
