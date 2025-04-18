"""
题面描述：
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

1. 左括号必须用相同类型的右括号闭合。
2. 左括号必须以正确的顺序闭合。
3. 每个右括号都有一个对应的相同类型的左括号。

示例 1：
    I: s = "()"
    O: True

示例 2：
    I: s = "()[]{}"
    O: True

示例 3：
    I: s = "([)]"
    O: False

示例 4：
    I: s = "(]"
    O: False

示例 5：
    I: s = "([{}])"
    O: True
"""

class Solution:
    def isValid(self,s: str) -> bool:
        brackets = {")":"(","]":"[","}":"{"}
        chars = list()
        for char in s:
            if char in brackets: # 处理右括号
                if not chars or chars[-1] != brackets[char]:
                    return False
                chars.pop()
            else: # 处理左括号
                chars.append(char)
        return not chars




if __name__ == '__main__':
    s = "()[]{}"
    sol = Solution()
    sol.isValid(s)