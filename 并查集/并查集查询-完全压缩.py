
# 完全压缩：正查询时，把被查询的节点到根节点的路径上是所有节点的父节点设置为根节点，从而减少树的深度
class UnionFind : 
    def __init__(self, n) :
        self.fa = [i for i in range(n)]
    
    def find(self,x) : 
        if self.fa[x] != x  : 
            self.fa[x] = self.find(self.fa[x])  # 完全压缩优化
        return self.fa[x]
    
    def union(self,x,y) : 
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y :
            return False 
        self.fa[root_x] = root_y
        return True 
        
        
    def is_connected(self,x,y) : 
        return self.find(x) == self.find(y)