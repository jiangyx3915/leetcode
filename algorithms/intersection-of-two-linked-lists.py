"""
编写一个程序，找到两个单链表相交的起始节点。

description: intersection-of-two-linked-lists(相交链表)
author: jiangyx3915
date: 2018/10/23

用环的思想来做，我们让两条链表分别从各自的开头开始往后遍历，当其中一条遍历到末尾时，我们跳到另一个条链表的开头继续遍历。两个指针最终会相等，
而且只有两种情况，一种情况是在交点处相遇，另一种情况是在各自的末尾的空节点处相等。
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None

        cur1 = headA
        cur2 = headB

        while cur1 != cur2:
            cur1 = cur1.next if cur1 else headB
            cur2 = cur2.next if cur2 else headA
        return cur1