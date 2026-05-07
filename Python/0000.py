from typing import List, Optional
from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        g = defaultdict(list)
        for (x, y), v in zip(equations, values):
            g[x].append((y, v))
            g[y].append((x, 1/v))
        
        res = []
        for x, y in queries:
            if x not in g or y not in g:
                res.append(-1.0)
            else:
                que = [(x, 1)]
                visited = set([x])
                found = False
                while que:
                    node, prod = que.pop()
                    if node == y:
                        res.append(prod)
                        found = True
                        break
                    for nei, v in g[node]:
                        if nei not in visited:
                            que.append((nei, prod * v))
                            visited.add(nei)
                if not found:
                    res.append(-1.0)
        return res

if __name__ == "__main__":
    print(Solution().calcEquation(equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]))