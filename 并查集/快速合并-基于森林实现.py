# !/usr/bin/python
# -*- coding: utf-8 -*-


# 基于随机森林实现的快速合并
# 使用一个森林存储所有的集合，每一颗树代表一个集合，树上的每个节点都是一个元素，树根节点为这个集合的代表元素
# 基于森林实现的并查集中，树中的节点都是指向父节点的

class UnionFind:
    def __init__(self, n):
        # 初始化：将每个元素的集合编号初始化为数组fa的下标索引
        self.fa = [i for i in range(n)]

    def find(self, x):
        # 查找元素根节点的集合编号内部实现方法
        # 递归查找元素的父节点，直到根节点
        while self.fa[x] != x:
            x = self.fa[x]
        return x    #  返回元素的根节点

    def union(self, x, y):
        # 合并操作：令其中一个集合的树根节点指向另一个集合树的根节点
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:  # x 和 y的根节点集合编号相同，说明x和y已经同属于一个集合
            return False
        self.fa[root_x] = root_y  # x的根节点连接到y的根节点，成为y的根节点的子节点
        return True

    def is_connected(self, x, y):
        # 查询操作：判断x和y的根节点是否相同，相同则说明x和y属于同一个集合
        return self.find(x) == self.find(y)
