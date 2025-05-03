# 1. 两数之和 答案解释

## 读题部分

题面描述：[LeetCode1-两数之和](https://leetcode.cn/problems/two-sum/description/)

题目中的两个数据，`target` 和 `nums`，对于它们，如果能找到一组数 `[i,j]`，使得 `nums[i] + nums[j] == target`，就返回 `[i,j]`；否则，就返回 `list()`。目标非常明确，可以直接着手做。

## 解法Ⅰ 暴力

先定下一个整数 `i`，并且记录下 `target - i` 作为待查找的值，如此遍历，直到符合题意即可。这样，我们容易想到利用 `for` 循环：

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
```

这里暴力嵌套两层循环，方向明确但是速度太慢。

**时间复杂度：** O(n<sup>2</sup>)，其中 n 是数组 `nums` 的长度。

**空间复杂度：** O(1)

## 解法Ⅱ 哈希表

根据题意，总是有：`nums[i] == target - nums[j]` 。于是我们设想，能不能通过遍历一次 `nums` 后，记录下每个可能的 `i` 值，并且在之后的过程中一一匹配呢？所以，此处利用查找速度为 O(1) 的哈希表（也就是 Python 中的字典）存储 `i` 的值。这样，我们只需要比对之后的元素是否在哈希表内，就得到了 `[i,j]`

所以，我们创建形如这样的字典：

```python
aftersum: dict = {num:i} # num 是当前查找到的元素，i 是当前元素的索引
```

为了获取它们，我们也需要使用 Python 内置函数 `enumerate()`，这样就能同时获取元素的索引和它本身了。

```python
nums: list = [1,5,4,3]
for i, num in enumerate(nums):
    print(i,num)
"""
输出结果：
0 1
1 5
2 4
3 3
"""
```

结合上面的思考过程，我们就能写出具体实现代码了。

```python
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        aftersum: dict = dict() # 空字典
        for i, num in enumerate(nums): # 此处 i 是索引，num 是元素
            if target - num in aftersum: 
                # 这个条件成立，也就意味着上面说到的 nums[i] == target - nums[j] 成立
                # 这样，我们就找到了正确答案
                return [i, aftersum[target - num]]
            	# 返回 当前元素的索引和对应元素的索引
                # 对应元素在之前已经存在 aftersum 中了
            aftersum[num] = i
            # 如果 aftersum 的键中找不到 target - num，就新建一个键值对
        return list()
```
