"""
description: reverse-linked-list(反转链表)
author: jiangyx3915
date: 2018/10/15
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        header = ListNode(0)
        
        while head:
            node = ListNode(head.val)
            node.next = header.next
            header.next = node
            head = head.next
        return header.next
