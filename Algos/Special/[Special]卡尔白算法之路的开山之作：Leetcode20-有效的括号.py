# 题面描述：https://leetcode.cn/problems/valid-parentheses/description/

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