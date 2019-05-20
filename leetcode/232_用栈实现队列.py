#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._in_stash = []
        self._out_stash = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._in_stash.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._out_stash:
            while self._in_stash:
                self._out_stash.append(self._in_stash.pop())
        
        return self._out_stash.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self._out_stash:
            while self._in_stash:
                self._out_stash.append(self._in_stash.pop())
        
        return self._out_stash[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return False if self._in_stash or self._out_stash else True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

