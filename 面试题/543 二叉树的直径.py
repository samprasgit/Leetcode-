# 最大深度遍历实现
# 对于树中的任意节点，经过该节点的最长路径长度可以由它的两个子树的深度之和来计算
# 具体实现步骤
# 对于每个节点，计算其左子树和右子树的深度
# 对于每个节点，其经过的最长路径长度即为其左子树深度加上右子树的深度
# 遍历完树的过程中，记录并更新最长路径长度的最大值
# 遍历完后后，得到的最大值就是树的直径


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
