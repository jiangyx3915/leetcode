<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->
# 题目描述

实现 `int sqrt(int x)` 函数。

计算并返回 x 的平方根，其中 x 是非负整数。

由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。

# 示例

示例 1:

```text

输入: 4
输出: 2

```

示例 2:

```text

输入: 8
输出: 2
说明: 8 的平方根是 2.82842...,
     由于返回类型是整数，小数部分将被舍去。

```

# 解题思路

使用二分查找，找其平方根

# 代码实现

```python

class Solution:
    def func(self, x):
        low, high = 0, x
        while low <= high:
            mid = (low + high) // 2
            sqt = mid * mid
            if sqt == x:
                return mid
            elif sqt > x:
                high = mid - 1
            elif sqt < x < (mid + 1) * (mid + 1):
                return mid
            else:
                low = mid + 1
        return low

```
