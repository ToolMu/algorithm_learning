#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if not head:
            return None
            
        if head.val == val:
            head = self.removeElements(head.next,val)
        else:
            head.next = self.removeElements(head.next,val)
        return head

    # def removeElements(self, head: ListNode, val: int) -> ListNode:
    #     while head is not None and head.val == val:
    #         head = head.next
        
    #     current = head
    #     while current is not None:
    #         if current.next is not None and current.next.val == val:
    #             current.next = current.next.next
    #         else:
    #             current = current.next
        
    #     return head
        

