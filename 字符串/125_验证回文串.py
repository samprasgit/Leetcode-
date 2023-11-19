# !/usr/bin/python
# -*- coding: utf-8 -*-
# 验证回文串 

class Solution:
    def isPalindrome(self, s) :
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s[ : len(s) >> 1 ] == s[ : - (len(s) >> 1) - 1 : - 1]


        
