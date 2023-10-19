# !/usr/bin/python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class MyLiknedList:
    def __init__(self):
        self.head = ListNode(0)  # 哨兵节点
        self.size = 0

    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        cur = self.head
        for _ in range(index + 1):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        self.addAtIndex(0, val)

    def addAtTail(self, val):
        self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        if index > self.size:
            return
        elif index < 0:
            index = 0
        self.size += 1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        val = ListNode(val)
        val.next = cur.next
        cur.next = val

    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        cur = self.head
        for _ in range(index):
            cur = cur.next
        cur.next = cur.next.next
