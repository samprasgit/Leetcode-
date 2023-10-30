# !/usr/bin/python
# -*- coding: utf-8 -*-


import collections


class Solution:
    def topologicalSortingKahn(self, graph):
        # 记录所有顶点入度
        indegrees = {u: 0 for u in graph}
        for u in graph:
            for v in graph[u]:
                indegrees[v] += 1  # 统计所有顶点入度

        # 将入度为0的顶点存入集S中
        S = collections.deque([u for u in indegees if indegrees[u] == 0])
        order = []

        while S:
            u = S.pop()  # 从集合中选择一个没有前驱的顶点 0
            order.append(u)
            for v in graph[u]:
                indegrees[v] -= 1
                if indegrees[v] == 0:
                    S.append(v)

        if len(indegrees) != len(order):
            return []
        return order

    def findOrder(self, n, edges):
        # 构建图
        graph = dict()
        for i in range(n):
            graph[i] = []

        for u, v in edges:
            graph[u].append(v)

        return self.topologicalSortingKahn(graph)
