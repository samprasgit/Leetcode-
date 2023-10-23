# !/usr/bin/python
# -*- coding: utf-8 -*-


class Soluiton:
    def calculate(self, s):
        stack = []
        num = 0
        sign = "+"
        for i in range(len(s)):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
            if s[i] in "+-*/" or i == len(s) - 1:
                if sign == "-":
                    num = -num
                if sign == "+":
                    pass
                if sign == "*":
                    num = num * stack.pop()
                if sign == "/":
                    num = int(num / stack.pop())
                stack.append(num)
                sign = s[i]
                num = 0
        return sum(stack)
