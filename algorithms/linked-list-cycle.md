<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

## 示例1

```text
输入：head = [3,2,0,-4], pos = 1
输出：true
解释：链表中有一个环，其尾部连接到第二个节点。
```

## 示例2

```text
输入：head = [1,2], pos = 0
输出：true
解释：链表中有一个环，其尾部连接到第一个节点。
```

## 示例3

```text
输入：head = [1], pos = -1
输出：false
解释：链表中没有环。
```

进阶：

你能用 O(1)（即，常量）内存解决此问题吗？

# 代码

## 使用快慢指针

```python
class Solution(object):
    def hasCycle(self, head):
        """
        使用快慢指针，如果链表有环则快指针会和慢指针相交
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False

        fast = head.next
        slow = head

        # 如果快指针和慢指针相交则存在环
        while fast.next and fast.next.next:
            if fast == slow:
                return True
            fast = fast.next.next
            slow = slow.next
        return False
```