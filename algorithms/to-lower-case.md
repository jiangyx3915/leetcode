<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

实现函数 ToLowerCase()，该函数接收一个字符串参数 str，并将该字符串中的大写字母转换成小写字母，之后返回新的字符串。

# 示例

示例 1

```text

输入: "Hello"
输出: "hello"

```

示例 2

```text

输入: "here"
输出: "here"

```

示例 3

```text

输入: "LOVELY"
输出: "lovely"

```

# 解题思路

大字母的ASCII码为 65~90，转成小写直接加上32即可

# 代码实现

```python

class Solution:
    def toLowerCase(self, str):
        result = ''
        for index in range(len(str)):
            cur = str[index]
            if 65 <= ord(cur) <= 90:
                result += chr(ord(cur) + 32)
            else:
                result += cur
        return result

```