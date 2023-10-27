# !/usr/bin/python
# -*- coding: utf-8 -*-


class Queue:
    # 初始化队列
    def __init__(self, size=100):
        self.size = size
        self.queue = [None for _ in range(size)]
        self.front = -1
        self.rear = -1

    # 判断队列是否为空
    def is_empty(self):
        return self.front == self.rear

    # 判断队列是否已满
    def is_full(self):
        return self.rear == self.size - 1

    # 入队操作
    def enqueue(self, value):
        if is_full():
            raise Exception("Queue is full")
        else:
            self.rear += 1
            self.queue[self.rear] = value

    # 出队操作
    def dequeue(self):
        if is_empty():
            raise Exception("Queue is empty")
        else:
            self.front += 1
            return self.queue[self.front]

    # 获取队头元素
    def front_value(self):
        if is_empty():
            raise Exception("Queue is empty")
        else:
            self.queue[self.front + 1]

    # 获取队尾元素
    def rear_value(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        else:
            return self.queue[self.rear]
