from typing import List
class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        m = len(land)
        n = len(land[0])
        res = []

        def explore(r1, c1):
            r2, c2 = r1, c1
            while r2 < m and land[r2][c1] == 1:
                c2 = c1
                while c2 < n and land[r2][c2] == 1:
                    land[r2][c2] = 0
                    c2 += 1
                r2 += 1
            return [r1, c1, r2 - 1, c2 - 1]

        for r1 in range(m):
            for c1 in range(n):
                if land[r1][c1] == 1:
                    coordinates = explore(r1, c1)
                    res.append(coordinates)
        return res

