from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        d = {}
        for i in range(1, n ** 2 + 1):
            d[i] = 0
        for i in range(n):
            for  j in range(n):
                d[grid[i][j]] += 1
        res = [0] * 2
        for k, v in d.items():
            if v == 2:
                res[0] = k
            elif v == 0:
                res[1] = k
        return res    