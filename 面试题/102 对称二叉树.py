# 递归实现对称二叉树


class Solution:
    def isSymmetric(self, root):
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        # 首先排除空节点的情况
        if left == None and right != None:
            return False
        elif left != None and right == None:
            return False
        elif left == None and right == None:
            return True
        # 删除空节点在排除数值不相等的情况
        elif left.val != right.val:
            return False

        # 左右节点不为空，且数值相等
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        isSame = outside and inside
        return isSame
