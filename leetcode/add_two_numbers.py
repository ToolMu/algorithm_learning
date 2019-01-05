# Definition for singly-linked list.
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
    print(add_data.val)
