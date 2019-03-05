### 只出现一次的数字

给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。

说明：

你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

示例 1:
```text
输入: [2,2,1]
输出: 1
```

示例 2:
```text
输入: [4,1,2,1,2]
输出: 4
```

### 解题思路

线性时间复杂度: 要求时间复杂度为O(n)
不使用额外空间: 要求空间复杂度为O(1)

#### 解法一

不考虑空间复杂度，可以考虑使用字典，数字每出现一次将其对应值加一。由于只有一个位数字出现一次，则可以最后获取value值为1的键即可

```python
from typing import List
from collections import defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = defaultdict(int)
        for i in nums:
            d[i] += 1
        return list(d.keys())[list(d.values()).index(1)]
```

#### 解法二

利用HashSet的特性，删除重复的数组元素，最后剩下一个单独的元素，返回即可

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = set()
        for i in nums:
            if i in d:
                d.remove(i)
            else:
                d.add(i)
        return d.pop()
```

#### 解法三(推荐)

根据异或运算的特点，相同的数字经过异或运算后结果为0，除单独出现一次的数字外，其他数字都是出现两次的，那么这些数字经过异或运算后结果一定是0。而任何数字与0进行异或运算都是该数字本身。所以对数组所有元素进行异或运算，运算结果就是题目的答案。

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        num = 0
        for i in nums:
            num = num ^ i
        return num
```

#### 解法四

通过对列表进行排序，判断当前元素和后一元素是否相等

```python
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != nums[i+1]:
                return nums[i+1]
        return nums[-1]
```