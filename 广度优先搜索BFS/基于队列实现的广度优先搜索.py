# !/usr/bin/python
# -*- coding: utf-8 -*-


import collections


class Solution:
    def bfs(self, graph, u):
        visited = set()  # 标记访问过的集合
        queue = collections.deque([])  # 使用queue存放临时节点

        visited.add(u)
        queue.append(u)

        while queue:
            u = queue.popleft()
            print(u)
            for v in graph[u]:
                if v not in visited:
                    visited.add(v)
                    queue.append(v)


graph = {
    "0": ["1", "2"],
    "1": ["0", "2", "3"],
    "2": ["0", "1", "3", "4"],
    "3": ["1", "2", "4", "5"],
    "4": ["2", "3"],
    "5": ["3", "6"],
    "6": []
}

# 基于队列实现的广度优先搜索
print(Solution().bfs(graph, "0"))