#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#
# https://leetcode-cn.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (51.67%)
# Total Accepted:    40.8K
# Total Submissions: 78.4K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# 将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 
# 
# 示例：
# 
# 输入：1->2->4, 1->3->4
# 输出：1->1->2->3->4->4
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        result_head = result_node = ListNode(-1)
        while l1:   # 慢原因之一
            if l2 and l1.val > l2.val:
                val = l2.val
                l2 = l2.next
            elif l2 and l1.val <= l2.val:
                val = l1.val
                l1 = l1.next
            else:
                result_node.next = l1
                break
            
            result_node.next = ListNode(val)
            result_node = result_node.next
        
        if l2:
            result_node.next = l2
        
        return result_head.next
        
