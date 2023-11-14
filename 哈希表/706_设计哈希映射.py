# !/usr/bin/python
# -*- coding: utf-8 -*-


# 假设数组足够长


class MyHashMap:
    def __init__(self):
        self.map = [-1] * 1000001

    def put(self, key, value):
        self.map[key] = value

    def get(self, key):
        self.map[key]

    def remove(self, key):
        self.map[key] -= 1
