class Trie:
    def __init__(self):
        self._root = {}
        self._end_char = '%%'

    def add(self, word):
        node = self._root
        for c in word:
            node = node.setdefault(c, {})
        node[self._end_char] = None

    def adds(self, words):
        for item in words:
            self.add(item)

    def find(self, word):
        node = self._root
        for c in word:
            if c not in node:
                return False
            node = node[c]
        return self._end_char in node


if __name__ == "__main__":
    words = ["the", "this", "there"]
    trie = Trie()
    trie.adds(words)
    print(trie.find("the"))
    print(trie.find("The"))

