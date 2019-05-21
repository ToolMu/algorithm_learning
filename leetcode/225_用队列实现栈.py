#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._work_queue = []
        self._help_queue = []
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self._work_queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if not len(self._work_queue):
            raise ValueError("this queue is empty")
        
        while len(self._work_queue) != 1:
            self._help_queue.append(self._work_queue[0])
            self._work_queue.remove(self._work_queue[0])
        
        pop_data = self._work_queue[0]
        self._work_queue.remove(pop_data)
        self._work_queue, self._help_queue = self._help_queue, self._work_queue

        return pop_data
        

    def top(self) -> int:
        """
        Get the top element.
        """
        w_len = len(self._work_queue)
        return self._work_queue[w_len-1] if w_len else self._help_queue[len(self._help_queue)-1]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not len(self._work_queue) and not len(self._help_queue)
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

