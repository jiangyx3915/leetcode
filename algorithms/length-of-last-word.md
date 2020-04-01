<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

# 示例

```python

输入: "Hello World"
输出: 5

```

# 解题思路

解法一

先去除字符串两边的空格，然后以空格分隔取最后一个单词的长度即可

解法二

使用以标记表示是否遇到空格，当标记为True时，初始化长度为1，否则就把长度增加一

# 代码实现

解法一

```python

class Solution:

    def func(self, s):
        return len(s.strip().split(' ')[-1])

```

解法二

```python

class Solution:

    def func(self, s):
        if not s:
            return 0
        length = 0
        flag = False
        for i in s:
            if i == " ":
                flag = True
                continue
            if flag is True:
                length = 0
                flag = False
            length += 1
        return length

```