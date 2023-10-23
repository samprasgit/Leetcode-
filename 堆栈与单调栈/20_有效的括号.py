# !/usr/bin/python
# -*- coding: utf-8 -*-


# 解题思路


class Solution:
    def isValid(self, s):
        if len(s) % 2 == 1:
            return False

        stack = list()

        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            elif ch == ")":
                if len(stack) != 0 and stack[-1] == "(":
                    stack.pop()
                else:
                    return False

            elif ch == "]":
                if len(stack) != 0 and stack[-1] == "[":
                    stack.pop()
                else:
                    return False

            elif ch == "}":
                if len(stack) != 0 and stack[-1] == "{":
                    stack.pop()
                else:
                    return False

        if len(stack) == 0:
            return True
        else:
            return False
