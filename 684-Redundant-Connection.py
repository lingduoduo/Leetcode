# ## Union Find Method
# class UnionFindSet:
#     def __init__(self, n):
#         self._parents = [i for i in range(n + 1)]
#         self._ranks = [1 for i in range(n + 1)]

#     def find(self, u):
#         while u != self._parents[u]:
#             self._parents[u] = self._parents[self._parents[u]]
#             u = self._parents[u]
#         return u

#     def union(self, u, v):
#         pu, pv = self.find(u), self.find(v)
#         if pu == pv: return False

#         if self._ranks[pu] < self._ranks[pv]:
#             self._parents[pu] = pv
#         elif self._ranks[pu] > self._ranks[pv]:
#             self._parents[pv] = pu
#         else:        
#             self._parents[pv] = pu
#             self._ranks[pu] += 1

#         return True

# class Solution:
#     def findRedundantConnection(self, edges):
#         """
#         :type edges: List[List[int]]
#         :rtype: List[int]
#         """

#         s = UnionFindSet(len(edges))

#         for edge in edges:
#             if not s.union(edge[0], edge[1]): return edge
#         return None

## DFS
'''
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
'''


class Solution:
    def findRedundantConnection(self, edges):
        self.d = dict()
        visited = set()
        
        for edge in edges:
            u = edge[0]
            v = edge[1]

            if self.haspath(u, v, visited):
                return edge
            
            self.d[u] = self.d.get(u, []) + [v]
            self.d[v] = self.d.get(v, []) + [u]
        return False
    
    def haspath(self, start, target, visited):
        print(start)
        print(target)
        print(self.d)
        
        if start == target:
            return True
        visited.add(start)
        
        if start not in self.d or target not in self.d:
            return False
        
        if start in self.d and target in self.d[start]:
            return True
        else:
            for node in self.d[start]:
                # if node in visited:
                #     continue
                if self.haspath(node, target, visited):
                    return True
            return False

if __name__ == '__main__':
    edges = [[1,2], [1,3], [2,3]]
    result = Solution().findRedundantConnection(edges)
    print(result)
    