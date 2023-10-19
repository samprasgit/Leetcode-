# !/usr/bin/python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head):
        if not head or not head.next:
            return head

        odd = head
        even_head = even = head.next
        if odd.next:
            odd.next = odd.next.next
            even.netx = even.next.next
            odd = odd.next
            even = even.next
        odd.next = even_head

        return head
