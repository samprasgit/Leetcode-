# !/usr/bin/python
# -*- coding: utf-8 -*-


def dfs_recursive(graph, u, visited):
    """
    graph 存储无向图的嵌套数组变量
    u 当前遍历边的开始节点
    visited 标记访问节点的集合
    """
    # 节点U已经访问
    visited.add(u)

    for v in graph[u]:
        # 节点V未访问
        if v not in visited:
            # 深度优先遍历搜索
            dfs_recursive(graph, v, visited)


graph = {"A": ["B", "C"], "B": ["A", "C", "D"], "C": ["A", "B", "D", "E"], "D": ["B", "C", "E", "F"], "E": ["C", "D"], "F": ["D", "G"], "G": []}

# 基于递归实现的深度优先搜索
visited = set()
print(dfs_recursive(graph, "A", visited))
