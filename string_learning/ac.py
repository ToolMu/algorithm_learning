class ACNode:
    def __init__(self):
        self.next = {}  # 子节点
        self.fail = None  # 失效跳转位置
        self.isWord = False  # 是否是一个词


class AhoCorasick:
    def __init__(self):
        self._root = ACNode()  # 构建根节点

    def insert(self, word):
        """
        添加操作
        :params word: 添加的词
        :return:
        """
        curr = self._root

        for i in range(len(word)):
            if word[i] not in curr.next.keys():
                curr.next[word[i]] = ACNode()

            curr = curr.next[word[i]]

        curr.isWord = True

    def make(self):
        """
        跳转位置  构建失效指针
        """
        tmp_queue = [self._root, ]
        while tmp_queue:
            temp = tmp_queue.pop()  # 位置节点
            for key, value in temp.next.items():  # 下属子节点
                if temp == self._root:  # 根节点的失效节点为自身
                    temp.next[key].fail = self._root
                else:
                    p = temp.fail
                    while p:
                        if key in p.next.keys():
                            temp.next[key].fail = p.next[key]
                            break
                        p = p.fail  # 无值匹配跳转至失效指针指向
                    if not p:  # 空数据的失效信息指向根节点
                        temp.next[key].fail = self._root
                tmp_queue.append(temp.next[key])

    def search(self, content):
        """
        AC搜索部分代码
        """
        p = self._root
        result = []
        start_word_index = 0

        for i in range(len(content)):
            word = content[i]  # 取得词
            while word not in p.next.keys() and p != self._root:  # 调整位置
                p = p.fail  # 失效数据移动

            if word in p.next.keys():
                if p == self._root:  # 词开始
                    start_word_index = i

                p = p.next[word]
            else:
                p = self._root

            if p.isWord:  # 词结束记录
                result.append((start_word_index, i))

        return result


if __name__ == '__main__':
    """
    -> |-> h -> e -> r -> s
       |     -> i -> s
       |-> s -> h -> e
    """
    ac = AhoCorasick()
    word_list = ["he", "she", "his", "hers"]
    for word in word_list:
        ac.insert(word)
    ac.make()
    print(ac.search('hers get his job!'))
    print('Over!!!')