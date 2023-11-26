# !/usr/bin/python
# -*- coding: utf-8 -*-



class UnionFind:  
    
    def __init__(self,n ) : 
        self.fa= [ i for i in range(n) ]
        self.rank = [1  for i in range(n)]
        
        
    def find(self,x,y) : 
        while self.fa[x] != x :
            self.fa[x]  = self.fa[self.fa[x]]
            x = self.fa[x]
        return x     
    
    def union(self,x,y) : 
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y : 
            return False
        
        if self.rank[root_x] < self.rank[root_y] :
            self.fa[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y] :
            self.fa[root_y] = root_x
        else :
            self.fa[root_y] = root_x
            self.rank[root_x] += 1
            
        return True 
    
    def is_connected(self,x,y) :
        return self.find(x) == self.find(y)
    
