#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (56.54%)
# Total Accepted:    12.4K
# Total Submissions: 22K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
# 
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
# 
# 示例:
# 
# 给定 1->2->3->4, 你应该返回 2->1->4->3.
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        res_head = ListNode(' ')
        res_head.next = head
        change_head = res_head
        first_mark = swap_mark = head

        while swap_mark:
            swap_mark = swap_mark.next
            if swap_mark:
                first_mark.next = swap_mark.next
                swap_mark.next = first_mark
                
                change_head.next = swap_mark
                change_head = first_mark
                
                first_mark = swap_mark = first_mark.next
        
        return res_head.next
        
