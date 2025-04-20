# -*- coding: utf-8 -*-

__author__ = 'Karlbaey'

from typing import Optional,List

class TreeNode:
    # 一个只有三个节点的二叉树，详见 4.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solutions():
    # 1. LeetCode2235-两整数相加
    # 题面描述：https://leetcode.cn/problems/add-two-integers/description/
    def sum(self, num1: int, num2: int) -> int:
        return num1+num2
    
    # 2. LeetCode2469-温度转换
    # 题面描述：https://leetcode.cn/problems/convert-the-temperature/description/
    def convertTemperature(self, celsius: float) -> list[float]:
        return [celsius+273.15,celsius*1.8+32]
    
    # 3. LeetCode2413-最小偶倍数
    # 题面描述：https://leetcode.cn/problems/smallest-even-multiple/description/
    def smallestEvenMultiple(self, n: int) -> int:
        return n if n % 2 == 0 else n*2
    
    # 4. LeetCode2236-判断根结点是否等于子结点之和
    # 题面描述：https://leetcode.cn/problems/root-equals-sum-of-children/description/
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return True if root.left.val + root.right.val == root.val else False
    
    # 5. LeetCode1486-数组异或操作
    # 题面描述：https://leetcode.cn/problems/xor-operation-in-an-array/description/
    def xorOperation(self, n: int, start: int) -> int:
        ans = 0
        for i in range(n):
            ans ^= start+2*i
        return ans
    
    # 6. LeetCode1512-好数对的数目
    # 题面描述：https://leetcode.cn/problems/number-of-good-pairs/description/
    def numIdenticalPairs_1(self, nums: list[int]) -> int: 
        # 解法一
        # 采用了两层 for 循环，是一种暴力解法
        ans = 0
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] == nums[j] and i<j:
                    ans += 1
        return ans

    def numIdenticalPairs_2(self, nums: list[int]) -> int:
        # 解法二
        # 使用字典减少了匹配次数
        d = dict()
        ans = 0
        for num in nums:
            if num in d:
                ans += d[num]
                d[num] += 1
            else:
                d[num] = 1
        return ans
    
    # 7. LeetCode1534-统计好三元组
    # 题面描述：https://leetcode.cn/problems/count-good-triplets/description/
    def countGoodTriplets_1(self, arr: list[int], a: int, b: int, c: int) -> int:
        # 解法一
        # 三层 for 循环，极其暴力，极其不优雅
        n = len(arr)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        ans += 1
        return ans
    
    def countGoodTriplets_2(self, arr: list[int], a: int, b: int, c: int) -> int:
        # 解法二
        # 这个解法很帅气，但我读不懂。来自灵茶山大佬：https://leetcode.cn/problems/count-good-triplets/solutions/3622921/liang-chong-fang-fa-bao-li-mei-ju-qian-z-apcv/
        idx = sorted(range(len(arr)), key=lambda i: arr[i])
        ans = 0

        for j in idx:
            y = arr[j]
            left = [arr[i] for i in idx if i < j and abs(arr[i] - y) <= a]
            right = [arr[k] for k in idx if k > j and abs(arr[k] - y) <= b]
            k1 = k2 = 0
            for x in left:
                while k2 < len(right) and right[k2] <= x + c:
                    k2 += 1
                while k1 < len(right) and right[k1] < x - c:
                    k1 += 1
                ans += k2 - k1
        return ans
    
    # 10. LeetCode709-转换成小写字母
    # 题面描述：https://leetcode.cn/problems/to-lower-case/description/
    def toLowerCase_1(self, s: str) -> str:
        # 解法一
        # 直接调用 Python 内置函数
        return s.lower()
    
    def toLowerCase_2(self, s: str) -> str:
        # 解法二
        # 假设 Python 没有提供 str.lower() 这样方便的函数，就需要通过 ASCII 转小写
        return "".join(chr(ochar | 32) if 65 <= (ochar := ord(char)) <= 90 else char for char in s)
        # 为了方便理解，下面是展开式。其中提到的变量 ans 并不是必要的
        #     ans = []
        #     for char in s:
        #         ochar = ord(char)  # 计算字符的 ASCII 值
        #         if 65 <= ochar <= 90:
        #             lower_char = chr(ochar | 32)
        #             ans.append(lower_char)
        #         else:
        #             ans.append(char)
        #     return "".join(ans)
    
    # 11. LeetCode258-各位相加
    # 题面描述：https://leetcode.cn/problems/add-digits/description/
    def addDigits(self, num: int) -> int:
        return (num-1)%9+1 if num >= 1 else 0
    
    # 12. LeetCode1281-整数中的各位积和之差
    # 题面描述：https://leetcode.cn/problems/subtract-the-product-and-sum-of-digits-of-an-integer/description/
    def subtractProductAndSum(self, n: int) -> int:
        prod, SUM = 1, 0 
        for num in str(n):
            prod *= int(num)
            SUM += int(num)
        return prod-SUM
    
    # 13. LeetCode231-2的幂
    # 题面描述：https://leetcode.cn/problems/power-of-two/description/
    def isPowerOfTwo(self, n):
        return n > 0 and n & (n - 1) == 0 # 特别优雅的一段代码，我很喜欢
    
    # 14. LeetCode326-3的幂
    # 题面描述：https://leetcode.cn/problems/power-of-three/description/
    def isPowerOfThree(self, n: int) -> bool:
        return True if n > 0 and 1162261467 % n == 0 else False
    
    # 15. LeetCode263-丑数
    # 题面描述：https://leetcode.cn/problems/ugly-number/description/
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        else:
            while n % 3 == 0:
                n /= 3
            while n % 5 == 0:
                n /= 5
            while n % 2 == 0:
                n /= 2
            return n == 1
    
    # 16. LeetCode1470-重新排列数组
    # 题面描述：https://leetcode.cn/problems/shuffle-the-array/description/
    def shuffle(self, nums: list[int], n: int) -> list[int]:
        ans = list()
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n])
            n += 1
        return ans
    
    # 17. LeetCode867-转置矩阵
    # 题面描述：https://leetcode.cn/problems/transpose-matrix/description/
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        i, j = len(matrix), len(matrix[0])
        ans = [[0] * i for num in range(j)]
        for m in range(i):
            for n in range(j):
                ans[n][m] = matrix[m][n]
        return ans
    
    # 18. LeetCode1422-分割字符串的最大得分
    # 题面描述：https://leetcode.cn/problems/maximum-score-after-splitting-a-string/description/
    def maxScore(self, s: str) -> int:
        r = s.count("1")
        l = ans = 0
        for i in s[:-1]:
            if i == "0":
                l += 1
            else:
                r -= 1
            ans = max(ans,l+r)
        return ans
    
    # 19. LeetCode2586-统计范围内的元音字符串数
    # 题面描述：https://leetcode.cn/problems/count-the-number-of-vowel-strings-in-range/
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        ans = 0
        vowels = "aeiou"
        for i in range(left,right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                ans += 1
        return ans

    # 20. LeetCode852-山脉数组的峰顶索引
    # 题面描述：https://leetcode.cn/problems/peak-index-in-a-mountain-array/description/
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)-1
        while l<r:
            m = l + (r - l) // 2
            if arr[m] < arr[m+1]:
                l = m + 1
            else:
                r = m
        return l