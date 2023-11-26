# !/usr/bin/python
# -*- coding: utf-8 -*-


# 基于随机森林实现的快速合并


class UnionFind:
    def __init__(self, n):
        self.fa = [i for i in range(n)]

    def find(self, x):
        while self.fa[x] != x:
            x = self.fa[x]
        return x

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False
        self.fa[root_x] = root_y
        return True

    def is_connected(self, x, y):
        return self.find(x) == self.find(y)
