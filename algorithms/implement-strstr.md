<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

实现 strStr() 函数。

给定一个 haystack 字符串和一个 needle 字符串，在 haystack 字符串中找出 needle 字符串出现的第一个位置 (从0开始)。如果不存在，则返回  -1。

# 示例

示例 1:

```text
输入: haystack = "hello", needle = "ll"
输出: 2
```

示例 2:

```text
输入: haystack = "aaaaa", needle = "bba"
输出: -1
```

# 解题思路

方法一：暴力法，子串逐一比较
方法二：

双指针法

* 移动 pn 指针，直到 pn 所指向位置的字符与 needle 字符串第一个字符相等。

* 通过 pn，pL，curr_len 计算匹配长度。

* 如果完全匹配（即 curr_len == L），返回匹配子串的起始坐标（即 pn - L）。

* 如果不完全匹配，回溯。使 pn = pn - curr_len + 1， pL = 0， curr_len = 0。

# 代码实现

方法一

```python
class Solution:
    def func(self, haystack, needle):
        h, l = len(haystack), len(needle)
        if l == 0:
            return 0

        for i in range(h - l + 1):
            if haystack[i: i+l] == needle:
                return i
        return -1
```

方法二
```python
class Solution:
    def func(self, haystack, needle):
        h, l = len(haystack), len(needle)
        if l == 0:
            return 0
        ph = 0
        while ph < h - l + 1:
            while ph < h -l + 1 and haystack[ph] != needle[0]:
                ph += 1

            cur = pl = 0
            while pl < l and ph < h and haystack[ph] == needle[pl]:
                pl += 1
                ph += 1
                cur += 1

            if cur == l:
                return ph - l

            # 回溯
            ph = ph - cur + 1

        return -1
```