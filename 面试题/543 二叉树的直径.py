# 最大深度遍历实现


class Solution:
    def diameterOfBinaryTree(self, root):
        self.ans = 1

        def depth(node):
            # 如果访问的节点为空，返回0
            if not node:
                return 0
            # 左子节点为根的字数的深度
            L = depth(node.left)
            # 右子节点为根的子树的深度
            R = depth(node.right)
            # 计算d_model 即 L+R+1 并更新 ans
            self.ans = max(self.ans, L + R + 1)
            # 返回改节点为根的子树的深度
            return max(L, R) + 1

        depth(root)
        return self.ans - 1
