
from typing import List
import collections
class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        adj = collections.defaultdict(set)
        for a, b in edges:
            adj[a].add(b)
            adj[b].add(a)
        print(adj)

        res = 0
        stack = []
        while len(adj) > 2:
            for u in adj:
                if len(adj[u]) == 1:
                    stack.append(u)
            for u in stack:
                v = adj[u].pop()
                adj.pop(u)
                adj[v].remove(u)
            stack = []
            res += 2

        return res + 1 if len(adj) == 2 else res

if __name__ == "__main__":
    res = Solution().treeDiameter(edges = [[0,1],[0,2]])
    print(res)

