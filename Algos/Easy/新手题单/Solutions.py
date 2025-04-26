# -*- coding: utf-8 -*-

__author__ = 'Karlbaey'

from collections import Counter
from typing import List,Optional

class ListNode:
    # 一个链表，详见 5.
    def __init__(self, val=0, next=None):
        self.val = val
        self.val.next = next

class Solutions:
    # 1. LeetCode1480-一维数组的动态和
    # 题面描述：https://leetcode.cn/problems/running-sum-of-1d-array/description/
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = ans[i-1]+nums[i]
        return ans
    
    # 2. LeetCode1342-将数字变成 0 的操作次数
    # 题面描述：https://leetcode.cn/problems/number-of-steps-to-reduce-a-number-to-zero/description/
    def numberOfSteps_1(self, num: int) -> int:
        # 解法一，反复计算
        ans = 0
        while num != 0:
            if num%2 == 0:
                num /= 2
            else:
                num -= 1
            ans += 1
        return ans
    
    def numberOfSteps_2(self, num: int) -> int:
        # 解法二：位运算求解
        return num.bit_length() + num.bit_count() - 1 if num else 0
    
    # 3. LeetCode1672-最富有客户的资产总量
    # 题面描述：https://leetcode.cn/problems/richest-customer-wealth/description/
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for i in accounts:
            if ans < sum(i):
                ans = sum(i)
        return ans
    
    # 4. LeetCode412-Fizz Buzz
    # 题面描述：https://leetcode.cn/problems/fizz-buzz/description/
    def fizzBuzz(self, n: int) -> List[str]:
        ans = list()
        for i in range(n):
            ans.append("")
            ans[i] = str(i+1)
            if (i+1) % 3 == 0:
                ans[i] = "Fizz"
            if (i+1) % 5 == 0:
                ans[i] = "Buzz"
            if (i+1) % 5 == 0 and (i+1) % 3 == 0:
                ans[i] = "FizzBuzz"
        return ans 
    
    # 5. LeetCode876-链表的中间结点
    # 题面描述：https://leetcode.cn/problems/middle-of-the-linked-list/
    def middleNode_1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 解法一，链表转数组后再行迭代
        ans = [head]
        while ans[-1].next:
            ans.append(ans[-1].next)
        return ans[len(ans) // 2]
    
    def middleNode_2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 解法二，双指针
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    # LeetCode383-赎金信
    # 题面描述：https://leetcode.cn/problems/ransom-note/description/
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        return Counter(ransomNote) <= Counter(magazine)