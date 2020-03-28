<!--
 * 26. 删除排序数组中的重复项
 * @LastEditors: jiang yixin
 * @Author: jiang yixin
 -->

# 题目描述

给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

# 示例

示例1

```text

给定数组 nums = [1,1,2],

函数应该返回新的长度 2, 并且原数组 nums 的前两个元素被修改为 1, 2。

你不需要考虑数组中超出新长度后面的元素。

```

示例2

```text

给定 nums = [0,0,1,1,1,2,2,3,3,4],

函数应该返回新的长度 5, 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4。

你不需要考虑数组中超出新长度后面的元素。

```

# 解题思路

设置两个指针，一个慢指针，一个快指针。只有当两个指针指向的值不一致时，将慢指针加一，然后将快指针的值赋值给慢指针。

# 代码实现

```python

class Solution:

    def func(self, nums):
        if len(nums) <= 1:
            return len(nums)

        cur = 0

        for i in range(1, len(nums)):
            if nums[cur] != nums[i]:
                cur += 1
                nums[cur] = nums[i]

        return cur + 1
```