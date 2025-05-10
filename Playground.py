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
nums: list = [2,1,4,3,5]
k: int = 10
window: int = 0
l: int = 0
r: int = 0
ans: int = 0

for r in range(len(nums)):
    window += nums[r]
    while window * (r - l + 1) >= k:
        window -= nums[l]
        l += 1
    ans += (r - l + 1)



print(ans)