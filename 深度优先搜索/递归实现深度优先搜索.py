# !/usr/bin/python
# -*- coding: utf-8 -*-


def dfs_recursive(graph, u, visited):
    # 节点U已经访问
    visited.add(u)

    for v in graph[u]:
        # 节点V未访问
        if v not in visited:
            # 深度优先遍历搜索
            dfs_recursive(graph, v, visited)
