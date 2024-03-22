# BFS实现
def isCompleteTree(root):
    """
    判断一棵二叉树是否是完全二叉树。

    :param root: TreeNode，二叉树的根节点
    :return: bool，如果二叉树是完全二叉树则返回 True，否则返回 False
    """
    if not root:
        return True

    queue = [root]
    end = False

    while queue:
        node = queue.pop(0)
        if not node:
            end = True
        else:
            if end:
                # 如果已经遇到了空节点，后面再出现非空节点，则不是完全二叉树
                return False
            queue.append(node.left)
            queue.append(node.right)

    return True
