# 深度优先遍历
# 1确定递归函数的参数和返回类型
# 2确定终止条件
# 首先计数器如何统计这一条路径的和呢？

# 不要去累加然后判断是否等于目标和，那么代码比较麻烦，可以用递减，让计数器count初始为目标和，然后每次减去遍历路径节点上的数值。

# 如果最后count == 0，同时到了叶子节点的话，说明找到了目标和。

# 如果遍历到了叶子节点，count不为0，就是没找到。
# 3确定单层递归的逻辑
# 因为终止条件是判断叶子节点，所以递归的过程中就不要让空节点进入递归了。

# 递归函数是有返回值的，如果递归函数返回true，说明找到了合适的路径，应该立刻返回。


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        if not root.left and not root.right and sum == root.val:
            return True
        return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(
            root.right, sum - root.val
        )
