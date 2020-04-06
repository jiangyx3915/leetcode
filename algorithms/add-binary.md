<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

# 示例

示例 1:

```text

输入: a = "11", b = "1"
输出: "100"

```

示例 2:

```text

输入: a = "1010", b = "1011"
输出: "10101"

```

提示：

```text

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

```

# 解题思路

模拟加法运算规则，从最低位加到最高位

# 代码实现

```python

class Solution:

    def func(self, a, b):
        carry = 0
        i = len(a) - 1
        j = len(b) - 1
        result = ''
        while i >= 0 or j >= 0:
            m = a[i] if i >= 0 else '0'
            n = b[j] if j >= 0 else '0'
            sum = m + n + carry
            carry = sum // 2
            result = f'{sum % 2}{result}'
            i -= 1
            j -= 1

        if carry != 0:
            result = f'1{result}'

        return result

```
