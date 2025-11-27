from typing import List
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        if n <= 1: return []

        res = []
        def dfs(n, start, path):
            if n == 1:
                res.append(path)
            for i in range(start, int(n**(0.5)) + 1):
                if n % i == 0:
                    res.append(path + [i, n // i])
                    dfs(n//i, i, path+[i])

        dfs(n, 2,[])
        return res