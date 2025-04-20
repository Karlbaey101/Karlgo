s = "1110"
"""
0|0111
"""
r = s.count("1")
l = ans = 0
print(s[:-1])
for i in s:
    if i == "0":
        l += 1
        print("Left score is",l)
    else:
        r -= 1
        print("Right score is",r)
    ans = max(ans,l+r)
print(ans,r+l)

# 这有个二叉树！
class TreeNode:
    def __init__(self,data):
        self.data = data # 给节点数据
        self.left = None # 左节点
        self.right = None # 右节点

tree = TreeNode(10)
tree.left = TreeNode(4)
tree.right = TreeNode(6)

print(tree.data == tree.left.data + tree.right.data)