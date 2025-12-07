from typing import List

class UnionFind:
    def __init__(self, n):
        self.par = list(range(n))
        self.size = [1] * n
    
    def find(self, x):
        if x != self.par[x]:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        self.par[rx] = ry

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        uf = UnionFind(26)  # 26 lowercase letters

        # 1. First, union all equalities
        for eq in equations:
            if eq[1:3] == "==":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                uf.union(x, y)

        # 2. Then, check all inequalities
        for eq in equations:
            if eq[1:3] == "!=":
                x = ord(eq[0]) - ord('a')
                y = ord(eq[3]) - ord('a')
                if uf.find(x) == uf.find(y):
                    return False

        return True

if __name__ == "__main__":
    res = Solution().equationsPossible(equations =["a==b","b!=a"])
    print(res)