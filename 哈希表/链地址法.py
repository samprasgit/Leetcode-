# !/usr/bin/python
# -*- coding: utf-8 -*-


class ChainingHashTable:
    class Node:
        def __init__(self, key):
            self.key = key
            self.next = None

    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def insert(self, key):
        index = self.hash_function(key)
        if self.table[index] is None:
            self.table[index] = self.Node(key)
        else:
            current = self.table[index]
            while current.next:
                current = current.next
            current.next = self.Node(key)

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        while current:
            if current.key == key:
                return index
            current = current.next
        return None
