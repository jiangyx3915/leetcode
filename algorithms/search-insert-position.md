<!--
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->

# 题目描述

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。

# 示例

示例1：

```text
输入: [1,3,5,6], 5
输出: 2
```

示例2:

```text
输入: [1,3,5,6], 2
输出: 1
```

示例3：

```text

输入: [1,3,5,6], 7
输出: 4

```

示例4:

```text

输入: [1,3,5,6], 0
输出: 0

```


# 解题思路

## 解法一、暴力穷举法

遍历数组，如果当前所指向的值大于等于目标值则返回当前位置。如果遍历完未找到则返回数组的长度

## 二分查找法

使用二分查找

# 代码实现

暴力穷举法

```python

class Solution:

    def func(self, nums, target):
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
        return len(nums)

```

```python

class Solution:

    def func(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = int((low + high) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return low

```