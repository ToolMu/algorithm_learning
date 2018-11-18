class ACNode:
    def __init__(self):
        self.next = {}
        self.fail = None
        self.is_word = False


class AhoCorasick:
    def __init__(self):
        self._root = ACNode()

    def insert(self, word):
        """
        add something

        """
