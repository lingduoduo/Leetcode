class UnionFindSet:
    def __init__(self, n):
        self._parents = [i for i in range(n + 1)]
        self._ranks = [1 for i in range(n + 1)]
    
    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u
    
    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
        elif self._ranks[pu] > self._ranks[pv]:
            self._parents[pv] = pu
        else:        
            self._parents[pv] = pu
            self._ranks[pu] += 1
        
        return True
        
class Solution:
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        
        s = UnionFindSet(len(edges))
        
        for edge in edges:
            if not s.union(edge[0], edge[1]): return edge
        return None
