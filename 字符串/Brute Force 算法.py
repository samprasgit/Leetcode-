# !/usr/bin/python
# -*- coding: utf-8 -*-


def brute_force_two_sum(arr, target):
    # 遍历数组中的每个元素
    for i in range(len(arr)):
        # 再次遍历数组，寻找与当前元素配对的元素
        for j in range(i + 1, len(arr)):
            # 检查当前配对的元素之和是否等于目标值
            if arr[i] + arr[j] == target:
                return (i, j)  # 返回满足条件的元素索引

    return None  # 如果没有找到满足条件的配对，则返回None

# 测试算法
arr = [2, 7, 11, 15]
target = 9
result = brute_force_two_sum(arr, target)
print("Index of numbers:", result if result else "No solution found")

