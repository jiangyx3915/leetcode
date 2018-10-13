"""
description: merge-two-sorted-lists(合并两个有序链表)
author: jiangyx3915
date: 2018/10/13

将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

解题思路:
    新建立一个新的链表。建立两个指针cur1和cur2，分别指向两个链表。然后只需要通过比较两个链表每个元素的大小，小的元素添加到新的链表中即可。
最后，我们要分别判断cur1和cur2是否是各自链表的末尾，如果不是，将剩余元素添加到新的链表末尾即可。
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        header = ListNode(0)
        cur = header
        cur1 = l1
        cur2 = l2
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                cur.next = cur1
                cur1 = cur1.next
            else:
                cur.next = cur2
                cur2 = cur2.next
            cur = cur.next

        if cur1:
            cur.next = cur1
        if cur2:
            cur.next = cur2

        return header.next
