from collections import defaultdict, deque
from typing import List
import math
import heapq

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        def dfs(r, cols, digs, odigs, path):
            if r == n:
                res.append(path)
                return 
            
            for c in range(n):
                if c in cols or (r - c) in digs or (r + c) in odigs:
                    continue
                row = "." * c + "Q" + "." * (n - c - 1)
                dfs(
                    r + 1,
                    cols | {c},
                    digs | {r - c},
                    odigs | {r + c},
                    path + [row]
                )
        
        dfs(0, set(), set(), set(), [])
        return res



if __name__ == "__main__":
    res = Solution().solveNQueens(n=4)
    print(res)
