# !/usr/bin/python
# -*- coding: utf-8 -*-

class Solution : 
    def insertINtoBST(self,root,val) : 
        if not root : 
            return TreeNode(val)
        

        if val < root.val : 
            root.left = self.insertINtoBST(root.left,val)
        if val> root.val:
            root.right = self.insertINtoBST(root.right,val)
            
        return root   
    
    
