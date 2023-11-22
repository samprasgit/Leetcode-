# !/usr/bin/python
# -*- coding: utf-8 -*-


# 二叉搜索树的查找 插入 删除  实现
# 首先，我们需要定义一个二叉搜索树的节点类，它包含一个值和两个子节点。

# 然后，我们需要定义一个二叉搜索树类，它包含一个根节点，并有插入、查找和删除的方法。

# 插入方法的步骤如下：

# 如果树为空，新节点就是根节点。
# 否则，我们比较新节点和当前节点的值。
# 如果新节点的值小于当前节点的值，我们将其插入到左子树。
# 如果新节点的值大于当前节点的值，我们将其插入到右子树。
# 查找方法的步骤如下：

# 如果树为空，返回None。
# 否则，我们比较目标值和当前节点的值。
# 如果目标值等于当前节点的值，返回当前节点。
# 如果目标值小于当前节点的值，我们在左子树中查找。
# 如果目标值大于当前节点的值，我们在右子树中查找。
# 删除方法的步骤如下：

# 首先，我们需要找到要删除的节点。
# 如果要删除的节点没有子节点，我们可以直接删除它。
# 如果要删除的节点只有一个子节点，我们可以将其子节点替换为当前节点。
# 如果要删除的节点有两个子节点，我们需要找到右子树中的最小节点来替换当前节点。



class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, node):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)

    def find(self, value):
        if self.root is None:
            return None
        else:
            return self._find(value, self.root)

    def _find(self, value, node):
        if value == node.value:
            return node
        elif value < node.value and node.left is not None:
            return self._find(value, node.left)
        elif value > node.value and node.right is not None:
            return self._find(value, node.right)

    def delete(self, value):
        self.root = self._delete(value, self.root)

    def _delete(self, value, node):
        if node is None:
            return node
        if value < node.value:
            node.left = self._delete(value, node.left)
        elif value > node.value:
            node.right = self._delete(value, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._findMin(node.right)
                node.value = temp.value
                node.right = self._delete(node.value, node.right)
        return node

    def _findMin(self, node):
        if node.left is None:
            return node
        else:
            return self._findMin(node.left)