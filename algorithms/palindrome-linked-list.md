# 题目描述

请判断一个链表是否为回文链表。

## 示例 1:

```text
输入: 1->2
输出: false
```

## 示例 2:

```text
输入: 1->2->2->1
输出: true
```

##进阶：
你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？

# 代码

## 栈实现


```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        时间复杂度 O(n)，空间复杂度 O(1)
        
        现将链表的值进行压栈，利用栈的后进先出的特性对链表进行回文判断
        """
        stack = []
        point = head
        while point:
            stack.append(point.val)
            point = point.next

        while head:
            if head.val != stack.pop():
                return False
            head = head.next
        return True
```

## 快慢指针实现


```python
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        """
        时间复杂度 O(n)，空间复杂度 O(1)
        
        使用快慢指针加上逆置链表来判断是否是回文链表
        """
        if not head or not head.next:
            return True
        fast = head.next
        slow = head

        # 使用快慢指针获取到中间节点
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # 逆置后面的链表
        cur, prev = slow.next, None
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        # 顺序比较前半段
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        return True
```
