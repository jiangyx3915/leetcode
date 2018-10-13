"""
description: delete-node-in-a-linked-list(删除链表中的节点)
author: jiangyx3915
date: 2018/10/13

请编写一个函数，使其可以删除某个链表中给定的（非末尾）节点，你将只被给定要求被删除的节点。

现有一个链表 -- head = [4,5,1,9]，它可以表示为:
    4 -> 5 -> 1 -> 9

说明:
    链表至少包含两个节点。
    链表中所有节点的值都是唯一的。
    给定的节点为非末尾节点并且一定是链表中的一个有效节点。
    不要从你的函数中返回任何结果。

结题思路
    由于没有办法得到node的前节点，我们只能通过将下一个节点的值复制到当前节点node，然后移除node的下一个节点来达到目
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next
