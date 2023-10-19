# !/usr/bin/python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution1:
    def isPalindroem(self, head):
        # 双指针
        vals = []
        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        return vals == vals[::-1]  # 列表切片


class Solution2:
    def isPalindroem(self, head):
        # 递归实现
        self.front_point = head

        def recursively_check(cur=head):
            if not recursively_check(cur.next):
                return False
            if self.front_point.val != cur.val:
                return False
            self.front_point = self.front_point.next

            return True

        return recursively_check()
