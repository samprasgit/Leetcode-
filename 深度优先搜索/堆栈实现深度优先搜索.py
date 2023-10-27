# !/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def dfs_stack(self, graph, u):
        """
        graph   存储无向图的嵌套数组变量
        u 当前起始点
        visited

        """
        # visited 存放访问过的节点
        # stack 用来存放节点访问记录
        visited, stack = set(), []

        stack.append([u, 0])  # 节点u，以及节点u的下一邻接节点放入栈中，下次将遍历graph[u,0]
        visited.add(u)  # 起始节点标记为已访问

        while stack:
            u, i = stack.pop()  # 取出节点u以及下一要访问的节点坐标i

            if i < len(graph[u]):
                v = graph[u][i]  # 取出邻接点
                stack.pop([u, i + 1])  # 下一次将遍历 graph[u][i+1]
                if v not in visited:
                    print(v)
                    stack.append([v, 0])  # 下一次将遍历graph[v][0]
                    visited.add(v)  # 节点V标记为已访问
