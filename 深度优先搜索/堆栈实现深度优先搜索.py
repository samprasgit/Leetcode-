# !/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def dfs_stack(self, graph, u):
        visited, stack = set(), []
        stack.append(u)
        while stack:
            u = stack.pop()
            if u not in visited:
                visited.add(u)
                stack.extend(graph[u])
        return visited
