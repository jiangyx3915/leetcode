"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。


"""
class Solution:
	def isValid(self, s):
		"""
		:type s: str
		:return bool
		"""
		stack = []
		mapping = {')': '(', ']': '[', '}': '{'}
		for ch in s:
			if ch in mapping:
				top_element = stack.pop() if stack else '#'
				if mapping[ch] != top_element:
					return False
			else:
				stack.append(ch)
		return not stack

