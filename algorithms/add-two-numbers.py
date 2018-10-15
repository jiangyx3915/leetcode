"""
给定两个非空链表来表示两个非负整数。位数按照逆序方式存储，它们的每个节点只存储单个数字。将两数相加返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = l1
        q = l2
        header = ListNode(0)
        cur = header
        flag = 0
        while p or q or flag:
            x = p.val if p else 0
            y = q.val if q else 0
            result = x + y + flag
            flag = int(result / 10)
            cur.next = ListNode(result % 10)
            cur = cur.next
            if p:
                p = p.next
            if q:
                q = q.next
        return header.next