
# 路径压缩（Path Compression）：在从底向上查找根节点的过程中，如果此时访问的节点不是根节点，我们可以把这个节点尽量向上移动一下，从而减少树的层数
# 隔代压缩：在查询时，两步一压缩，一直循环执行[把当前节点指向它的父节点的父节点]这样的操作，从而减少树的深度
class UnionFind : 
    def __init__(self, n) :
        self.fa = [i for i in range(n)]
    
    def find(self,x) : 
        while self.fa[x] != x : 
            self.fa[x] = self.fa[self.fa[x]]
            x = self.fa[x]
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