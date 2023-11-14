# !/usr/bin/python
# -*- coding: utf-8 -*-


class Solution:
    def intersection(self, nums1, nums2):
        # 判读数组是否为空
        if not nums1 or not nums2:
            return []

        # 初始化哈希表
        hash = {}
        # 存放结果的列表
        res = []

        for i in nums1:
            if not hash.get(i):
                hash[i] = 1

        for j in nums2:
            if hash.get(j):
                res.append(j)
            hash[j] = 0

        return res
