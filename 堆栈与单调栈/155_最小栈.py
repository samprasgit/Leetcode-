# !/usr/bin/python
# -*- coding: utf-8 -*-


# 解题思路
# 使用辅助栈 类似一个元组 楚储存 当前元素值和栈内最小值


class MiniStack:
    def __init__(self):
        self.stack = []

    def push(self):
        if not self.stack:
            self.stack.append((x, x))
        else:
            self.stack.append((x, min(x, self.stack[-1][-1])))

    def pop(self):
        self.stack.pop()

    def top(self):
        return self.stack[-1][0]

    def get_mix(self):
        return self.stack[-1][1]
