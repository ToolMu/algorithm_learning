#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#
# https://leetcode-cn.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (31.86%)
# Total Accepted:    75.3K
# Total Submissions: 236.3K
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# 给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
# 
# 如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
# 
# 您可以假设除了数字 0 之外，这两个数都不会以 0 开头。
# 
# 示例：
# 
# 输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
# 输出：7 -> 0 -> 8
# 原因：342 + 465 = 807
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

## 解法2可以将链表转换为数字数字之和而后拆分  效率不如直接用链表的高

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = 0
        head = n = ListNode(-1)
        while l1 or l2 or res:
            val_1 = val_2 = 0
            if l1:
                val_1 = l1.val
                l1 = l1.next
            if l2:
                val_2 = l2.val
                l2 = l2.next

            res_sum = val_1 + val_2 + res
            n_val = res_sum % 10
            res = res_sum // 10

            n.next = ListNode(n_val)
            n = n.next

        head = head.next
        return head


if __name__ == "__main__":
    LNa1 = ListNode(3)
    LNa2 = ListNode(4)
    LNa3 = ListNode(2)
    LNa3.next = LNa2
    LNa2.next = LNa1
    LNb1 = ListNode(4)
    LNb2 = ListNode(6)
    LNb3 = ListNode(5)
    LNb3.next = LNb2
    LNb2.next = LNb1

    solution = Solution()
    add_data = solution.addTwoNumbers(LNa3, LNb3)

    while add_data.next:
        print(add_data.val)
        add_data = add_data.next
