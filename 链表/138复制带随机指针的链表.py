# !/usr/bin/python
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head):
        # 拼接+拆分
        if not head:
            return head
        cur = head
        while cur:
            tmp = Node(cur.val, cur.next, None)
            cur.next = tmp
            cur = tmp.next
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next
            cur = res = head.next
            pre = head
            while cur.next:
                pre.next = pre.next.next
                cur.next = cur.next.next
                pre = pre.next
                cur = cur.next
            pre.next = None
            return res
