### 求众数

给定一个大小为 n 的数组，找到其中的众数。众数是指在数组中出现次数大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在众数。

示例 1:
```text
输入: [3,2,3]
输出: 3
```
示例 2:
```text
输入: [2,2,1,1,1,2,2]
输出: 2
```

### 解题思路

#### 解法一

既然题目中已经表明众数必存在并且众数的数占有数组长度的至少一半，因此可以先将数组排序，接着取中间值即可获取到众数

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[int(len(nums)/2)]
```

#### 解法二

摩尔投票法

我们现将数组中的第一个数假设为众数，然后进行统计其出现的次数，如果遇到同样的数，则计数器自增1，否则计数器自减1，如果计数器减到了0，则更换下一个数字为候选者。这是一个很巧妙的设定，也是本算法的精髓所在，为啥遇到不同的要计数器减1呢，为啥减到0了又要更换候选者呢？首先是有那个强大的前提存在，一定会有一个出现超过半数的数字存在，那么如果计数器减到0了话，说明目前不是候选者数字的个数已经跟候选者的出现个数相同了，那么这个候选者已经很weak，不一定能出现超过半数，我们选择更换当前的候选者。那有可能你会有疑问，那万一后面又大量的出现了之前的候选者怎么办，不需要担心，如果之前的候选者在后面大量出现的话，其又会重新变为候选者，直到最终验证成为正确的众数

```python
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = count = 0
        for i in nums:
            if count == 0:
                major = i
                count += 1
            else:
                count = count + 1 if i == major else count - 1
        return major
```