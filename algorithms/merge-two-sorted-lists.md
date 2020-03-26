# 题目描述

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

# 示例

```text
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
```

# 解题思路

先设定一个头结点，然后通过遍历两个链表将较小的节点追加到新链表后，等到两个链表中有一个被遍历完之后，再将剩下的一个链表追加到新链表之后。


# 代码实现

```python
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        header = ListNode(0)
        cur = header

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                l2 = l2.next
            cur = cur.next

        if l1 is not None:
            cur.next = l1
        if l2 is not None:
            cur.next = l2

        return header.next
```