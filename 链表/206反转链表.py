# !/usr/bin/python
# -*- coding: utf-8 -*-


# 反转链表  双指针和递归实现
class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head):
        # 双指针实现爱你
        pre, cur = None, head
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre


class Solution2:
    def reverseList(self, head):
        # 递归实现
        if head is None or head.next is None:
            return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head


head = [1, 2, 3, 4, 5]
s = Solution2()
print(s.reverseList(head))
