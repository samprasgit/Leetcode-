# !/usr/bin/python
# -*- coding: utf-8 -*-


class UnionFind:
    # 初始化：将每个元素的集合编号初始化为数组下标索引
    def __init__(self, n):
        self.ids = [i for i in range(n)]

    # 查找元素所属集合编号内部实现方法
    def find(self, x):
        return self.ids[x]

    # 合并操作：将集合x和集合y合并成一个集合
    def union(self, x, y):
        x_id = self.find(x)
        y_id = self.find(y)

        if x_id == y_id:
            return False

        # 将2个集合的集合编号改为一致
        for i in range(len(self.ids)):
            if self.ids[i] == y_id:
                self.ids[i] = x_id
        return True

    # 查询操作:判断x和y是否属于同一个集合
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)

## 这种方式实现简单，但效率不高，每次合并操作都需要遍历整个数组