#
# @lc app=leetcode.cn id=25 lang=python3
#
# [25] k个一组翻转链表
#
# https://leetcode-cn.com/problems/reverse-nodes-in-k-group/description/
#
# algorithms
# Hard (47.96%)
# Total Accepted:    7.1K
# Total Submissions: 14.5K
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给出一个链表，每 k 个节点一组进行翻转，并返回翻转后的链表。
# 
# k 是一个正整数，它的值小于或等于链表的长度。如果节点总数不是 k 的整数倍，那么将最后剩余节点保持原有顺序。
# 
# 示例 :
# 
# 给定这个链表：1->2->3->4->5
# 
# 当 k = 2 时，应当返回: 2->1->4->3->5
# 
# 当 k = 3 时，应当返回: 3->2->1->4->5
# 
# 说明 :
# 
# 
# 你的算法只能使用常数的额外空间。
# 你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
# 
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = jump = ListNode(0)
        dummy.next = left = right = head
        
        while True:
            count = 0
            while right and count < k:
                right = right.next
                count += 1

            if count == k:
                # 1->2->3->4 ==> 3->2->1->4
                pre, cur = right, left
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur
                # 0->1->2->3->4 ==> 0->3->2->1->4
                jump.next, jump, left = pre, left, right
            else:
                return dummy.next


