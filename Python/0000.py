from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math

from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = ((1, 0), (-1, 0), (0, 1), (0, -1))
        area = {}

        def dfs(i: int, j: int, idx: int) -> int:
            if i < 0 or i >= n or j < 0 or j >= n or grid[i][j] != 1:
                return 0
            
            grid[i][j] = idx  
            area = 1
            for di, dj in dirs:
                area += dfs(i + di, j + dj, idx)
            
            return area


        idx = 2
        res = 0

        # 1) label islands and compute areas
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    area[idx] = dfs(i, j, idx)
                    best = max(best, area[idx])
                    idx += 1

        # If there is no 0, answer is whole grid (already best)
        # If there is no 1, best is 0 and flipping gives 1 (handled below)

        # 2) try flipping each 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    seen = set()
                    total = 1
                    for di, dj in dirs:
                        ni, nj = i + di, j + dj
                        if 0 <= ni < n and 0 <= nj < n:
                            k = grid[ni][nj]
                            if k > 1 and k not in seen:
                                seen.add(k)
                                total += area[k]
                    res = max(res, total)

        return res



if __name__ == "__main__":
    res = Solution().minBitwiseArray(nums = [2,3,5,7])
    print(res)




