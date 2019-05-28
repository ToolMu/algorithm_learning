#
# @lc app=leetcode.cn id=208 lang=python3
#
# [208] 实现 Trie (前缀树)
#
class Node:
    def __init__(self):
        self.next = {}  # 子节点
        self.fail = None  # 失效跳转位置
        self.isWord = False  # 是否是一个词


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._root = Node()
        
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr = self._root

        for i in range(len(word)):
            if word[i] not in curr.next.keys():
                curr.next[word[i]] = Node()

            curr = curr.next[word[i]]

        curr.isWord = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr = self._root
        for item in word:
            if item not in curr.next:
                return False
            curr = curr.next[item]
        return curr.isWord
        
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr = self._root
        for item in prefix:
            if item not in curr.next:
                return False
            curr = curr.next[item]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

