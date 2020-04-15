<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

# 题目实例

示例 1:

```text
输入: 1->1->2
输出: 1->2
```

示例 2:

```
输入: 1->1->2->3->3
输出: 1->2->3
```

# 解题思路

循环遍历链表，判断当前节点和后续节点

# 代码实现

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur and cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head

```