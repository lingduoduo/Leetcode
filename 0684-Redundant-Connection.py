#######Union Find Method
###class UnionFindSet:
###    def __init__(self, n):
###        self._parents = [i for i in range(n + 1)]
###        self._ranks = [1 for i in range(n + 1)]

###    def find(self, u):
###        while u != self._parents[u]:
###            self._parents[u] = self._parents[self._parents[u]]
###            u = self._parents[u]
###        return u

###    def union(self, u, v):
###        pu, pv = self.find(u), self.find(v)
###        if pu == pv: return False

###        if self._ranks[pu] < self._ranks[pv]:
###            self._parents[pu] = pv
###        elif self._ranks[pu] > self._ranks[pv]:
###            self._parents[pv] = pu
###        else:        
###            self._parents[pv] = pu
###            self._ranks[pu] += 1

###        return True

###class Solution:
###    def findRedundantConnection(self, edges):
###        """
###        :type edges: List[List[int]]
###        :rtype: List[int]
###        """

###        s = UnionFindSet(len(edges))

###        for edge in edges:
###            if not s.union(edge[0], edge[1]): return edge
###        return None

####DFS
'''
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
'''


class Solution:
    
    def findRedundantConnection(self, edges):
        d = dict()
        
        for edge in edges:
            u = edge[0]
            v = edge[1]
            
            if self.haspath(u, v, d, []):
                return edge
            
            d[u] = d.get(u, []) + [v]
            d[v] = d.get(v, []) + [u]
        return []
    
    def haspath(self, start, target, d, visited):
        if start == target:
            return True
        visited.append(start)
        
        if start not in d or target not in d:
            return False
        
        if start in d and target in d[start]:
            return True
        
        while visited:
            startnode = visited.pop(0)
            visited += d[startnode]
            
            for node in d[startnode]:
                d[startnode].remove(node)
                d[node].remove(startnode)
                
                if self.haspath(node, target, d, visited):
                    return True
            return False


if __name__ == '__main__':
    edges = [[1, 2], [1, 3], [2, 3]]
    result = Solution().findRedundantConnection(edges)
    print(result)
    #
    ###edges = [[1,2], [2,3], [3,4], [1,4], [1,5]]
    ###result = Solution().findRedundantConnection(edges)
    ###print(result)
    
    ###edges = [[1,2],[2,3],[2,4],[4,5],[1,5]]
    ###result = Solution().findRedundantConnection(edges)
    ###print(result)
