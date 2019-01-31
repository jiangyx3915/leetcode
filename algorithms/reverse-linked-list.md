### 反转一个单链表

示例:
```text
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
```

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
```

思路一：  
1、创建一个 header 节点。  
2、遍历链表，每次创建一个节点值和当前节点相同的，然后把 next 指向 header 节点的 next ，再将 header 节点的 next 指向创建节点。  
3、最后返回 header 节点的 next 节点即可。

```python
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
        
```