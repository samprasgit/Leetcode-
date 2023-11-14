# !/usr/bin/python
# -*- coding: utf-8 -*-


# 线性探测实现
class LinearProbingHashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            index = (index + 1) % self.size
        self.table[index] = key

    def search(self, key):
        index = self.hash_function(key)
        while self.table[index] is not None:
            if self.table[index] == key:
                return index
            index = (index + 1) % self.size
        return None
