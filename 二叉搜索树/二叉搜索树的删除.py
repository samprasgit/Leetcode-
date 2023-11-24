# !/usr/bin/python
# -*- coding: utf-8 -*-


class Soluttion : 
    
    def deleteNode(self,root,val):
        if not root : 
            return TreeNode(val)

        if root.val > val : 
            root.left = self.deleteNode(root.left,val) 
            return root 
        elif root.val < val : 
            root.right = self.deleteNode(root.right,val) 
            return root  
        
        else : 
            if not root.left: 
                return root.right
            elif not root.right : 
                return root.left 
            else: 
                curr = root.right 
                while curr.left : 
                    curr = curr.left 
                curr.left = root.left  
                return root.right    