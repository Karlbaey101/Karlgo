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

nums = [9,6,2,5,8,7,2]
prefsum = [0]
for i in range(len(nums)):
    prefsum.append(prefsum[-1]+nums[i])
prefsum2 = list(accumulate(nums))
print(prefsum2)

# 这有个链表！
class ListNode:
    # 一个链表，详见 5.
    def __init__(self, val=0, next=None):
        self.val = val
        self.val.next = next

llist = ListNode()
a = [llist]
print(a)