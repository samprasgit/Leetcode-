# !/usr/bin/python
# -*- coding: utf-8 -*-


from collections import Counter


class Solution:
    def intersect(self, nums1, nums2):
        if len(nums2) < len(nums1):
            return self.intersect(nums2, nums1)

        res = []
        c = Counter(nums1)
        for n in nums2:
            if n in c:
                res.append(n)
                c[n] -= 1
                if c[n] == 0:
                    c.pop(n)

        return res
