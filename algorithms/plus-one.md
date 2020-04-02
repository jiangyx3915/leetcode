<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

# 示例

示例1：

```python

输入: [1,2,3]
输出: [1,2,4]
解释: 输入数组表示数字 123。

```

示例2:

```python

输入: [4,3,2,1]
输出: [4,3,2,2]
解释: 输入数组表示数字 4321。

```

# 解题思路

有两种情况：最高位进位和最高位不进位。

最高位进位

如果是最高位进位则低位必须都为9，且加一后皆为0。因此需要初始化一个长度为length+1的数组，首位置为1代表进位

最高位不进位

如果最高位不进位，则无需新数组，后续的数字由低位计算而来

# 代码实现

```python

class Solution:
    def func(self, digits):
        carry = 1 # 进位

        for i in range(len(digits)-1, -1, -1):
            # 如果不进位了，则直接返回
            if carry == 0:
                return digits

            tmp = digits[i] + carry

            # 最高位不为9则表示进位为0
            carry = tmp // 10
            digits[i] = tmp % 10

        # 最高位进位则需要创建一个新数组，并且首位为1
        if carry != 0:
            return [1] + digits

        return digits

```