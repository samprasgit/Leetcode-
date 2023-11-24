# !/usr/bin/python
# -*- coding: utf-8 -*-


class Solution : 
    
    def insertINtoBST(self,root,val): 
        if not root :
            return TreeNode(val) 
        
        if val < root.val :  
            root.left = self.insertINtoBST(root.left,val)
        if val > root.val: 
            root.right = self.insertINtoBST(root.right,val)  
            
        return root 
    
    
    def buildBST(self,nums):
        root = TreeNode(val)
        for num in nums : 
            root = self.insertINtoBST(root,num)
        return root
    
    