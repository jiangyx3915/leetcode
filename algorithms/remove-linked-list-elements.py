"""
description: remove-linked-list-elements(移除链表元素)
author: jiangyx3915
date: 2018/10/15

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        header = ListNode(0)
        header.next = head
        cur = head
        before = header
        while cur:
            if cur.val == val:
                before.next = cur.next
                cur = before.next
            else:
                cur = cur.next
                before = before.next
        return header.next
        