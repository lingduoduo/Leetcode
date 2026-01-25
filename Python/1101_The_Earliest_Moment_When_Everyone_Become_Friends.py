
class UF:

    def __init__(self, n):
        self.par = list(range(n))
    
    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]
    
    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        self.par[px] = py
        return True

class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])

        uf = UF(n)
        groups = n
        for ts, x, y in logs:
            if uf.union(x, y):
                groups -= 1
            if groups == 1:
                return ts
        return -1


