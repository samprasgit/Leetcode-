# !/usr/bin/python
# -*- coding: utf-8 -*-

class TreeNode : 
    def __init__(self,val=0,left=None,right=None) : 
        self.val = val 
        self.left = left 
        self.right = right  
        
        
    # 递归实现
    def isValidBST(self,root) : 
        def helper(self,node,lower = float("-inf"),upper = float("inf")): 
            
            if not node : 
                return True 
            val = node.val 
            if val <= lower or val >= upper  : 
                return False  
            
            if not helper(node.left,lower,val) : 
                return False 
            
            if not helper(node.right,val,upper) : 
                return False 
            
            return True
        
        return helper(root)  
