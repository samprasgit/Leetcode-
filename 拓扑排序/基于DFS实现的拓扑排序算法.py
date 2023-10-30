# !/usr/bin/python
# -*- coding: utf-8 -*-


import collections


class Solution:
    def topologicalSortingDFS(self, graph):
        visited = set()  # 记录当前节点是否被访问过
        onStack = set()  # 记录同一次深搜时，当前顶点是否被访问过
        order = []  # 记录拓扑排序的顺序
        hasCycle = False  # 用于判断是否存在环

        def dfs(u):
            nonlocal hasCycle
            if u in onStack:
                hasCycle = True
            if u in visited or hasCycle:
                return

            visited.add(u)
            onStack.add(u)

            for v in graph[u]:
                dfs(u)

            order.append(u)
            onStack.append(u)

        for u in graph:
            if u not in visited:
                dfs(u)

        if hasCycle:
            return []

        order.reverse()
        return order

    def findOrder(self, n, edges):
        # 构建图
        graph = dict()
        for i in range(n):
            graph[i] = []
        for v, u in edges:
            graph[v].append(u)

        return self.topologicalSortingDFS(graph)
