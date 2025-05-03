# 这有个二叉树！
from itertools import accumulate

class TreeNode:
    def __init__(self,data):
        self.data = data # 给节点数据
        self.left = None # 左节点
        self.right = None # 右节点

tree = TreeNode(10)
tree.left = TreeNode(4)
tree.right = TreeNode(6)

nums: list = [1,5,4,3]
target = 7
prefsum = [0]
for i in range(len(nums)):
    prefsum.append(prefsum[-1]+nums[i])
prefsum2 = list(accumulate(nums))

# 这有个链表！
class ListNode:
    # 一个链表，详见 5.
    def __init__(self, val=0, next=None):
        self.val = val
        self.val.next = next


"""
aftersum = dict()
for i, num in enumerate(nums):
    print(i,num)
    if target - num in aftersum:
        print("现在的字典是：",aftersum)
        print("将要找的数字是：",target-num)
        print("答案是：",[i,aftersum[target-num]])
    aftersum[num] = i
    print("将要找的数字是：",target-num)
    print("现在的字典是：",aftersum)
print(list())
"""
for i, num in enumerate(nums):
    print(i,num)