# !/usr/bin/python
# -*- coding: utf-8 -*-


# 堆栈的顺序存储实现
class Stack:
    # 初始化空栈
    def __init__(self, size=100):
        self.stack = []
        self.size = size
        self.top = -1

    # 判断栈是否为空
    def is_empty(self):
        return self.top == -1

    # 判断栈是否已满
    def is_full(self):
        return self.top == self.size - 1

    # 入栈操作
    def push(self, value):
        if self.is_full():
            raise Exception("Stack is full")
        else:
            self.stack.append(value)
            self.top += 1

    # 出栈操作
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            self.top -= 1
            return self.stack.pop()

    # 获取栈顶元素
    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        else:
            return self.stack[self.top]
