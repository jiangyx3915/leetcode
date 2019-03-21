### 验证回文串

给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

```text
输入: "A man, a plan, a canal: Panama"
输出: true
```

示例 2:

```text
输入: "race a car"
输出: false
```

### 解题思路

#### 解法一

将字符串中的非数字和字母取出拼接成一个新的字符串，接着让此字符串和其翻转的字符串相比较

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        s = ''.join(filter(str.isalnum, s)).lower()
        print(s)
        return s == s[::-1]
```

#### 解法二（推荐）

使用双指针分别从字符的开头和结尾处开始遍历整个字符串，如果遇到非字母数字的字符就跳过，继续往下找，直到找到下一个字母数字或者结束遍历，如果遇到大写字母，就将其转为小写。等左右指针都找到字母数字时，比较这两个字符，若相等，则继续比较下面两个分别找到的字母数字，若不相等，直接返回false，时间复杂度为O(n)。

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
            elif not s[end].isalnum():
                end -= 1
            elif s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True
```