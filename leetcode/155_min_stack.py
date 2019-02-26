#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#
# https://leetcode-cn.com/problems/min-stack/description/
#
# algorithms
# Easy (46.67%)
# Total Accepted:    14.7K
# Total Submissions: 31.4K
# Testcase Example:  '["MinStack","push","push","push","getMin","pop","top","getMin"]\n[[],[-2],[0],[-3],[],[],[],[]]'
#
# 设计一个支持 push，pop，top 操作，并能在常数时间内检索到最小元素的栈。
# 
# 
# push(x) -- 将元素 x 推入栈中。
# pop() -- 删除栈顶的元素。
# top() -- 获取栈顶元素。
# getMin() -- 检索栈中的最小元素。
# 
# 
# 示例:
# 
# MinStack minStack = new MinStack();
# minStack.push(-2);
# minStack.push(0);
# minStack.push(-3);
# minStack.getMin();   --> 返回 -3.
# minStack.pop();
# minStack.top();      --> 返回 0.
# minStack.getMin();   --> 返回 -2.
# 
# 
#
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._min_stack = []
        self._normal_stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self._normal_stack:
            self._normal_stack.append(x)
            self._min_stack.append(x)
        else:
            min_stack_top = self._min_stack[-1]
            self._normal_stack.append(x)
            self._min_stack.append(min(min_stack_top, x))
        
    def pop(self):
        """
        :rtype: void
        """
        if not self._normal_stack:
            raise ValueError
        else:
            self._normal_stack.pop()
            self._min_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self._normal_stack[-1]
        

    def getMin(self):
        """
        :rtype: int
        """
        return self._min_stack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
