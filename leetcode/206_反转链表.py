#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # def reverseList(self, head: ListNode) -> ListNode:
    #     recerse_node = ListNode(-1)
    #     while head:
    #         new_node = head
    #         head = head.next

    #         new_node.next = recerse_node.next
    #         recerse_node.next = new_node
        
    #     return recerse_node.next
    def reverseList(self, head: ListNode) -> ListNode:
        """递归处理上述为迭代处理"""
        if not head or not head.next: 
            return head
        
        reverse_list = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        
        return reverse_list
        

