from typing import List
from collections import Counter
import heapq
import re
from collections import defaultdict, deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(i, j):
            if i < 0 or i >= len(grid) or j < 0 or j>= len(grid[0]) or grid[i][j] == "0": return 

            grid[i][j] == "0"
            for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                dfs(i + dx, j + dy)

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    res += 1
        return res

if __name__ == "__main__":
    res = Solution().lengthOfLongestSubstringKDistinct(s = "eceba", k = 2)
    print(res)