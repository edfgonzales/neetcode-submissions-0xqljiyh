class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        pu = self.find(u)
        pv = self.find(v)
        if pu == pv:
            return False
        if self.size[pu] < self.size[pv]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.size[pu] += self.size[pv]
        return True

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)
        count = n

        for u, v in edges:
            if dsu.union(u, v):
                count -= 1
        return count

