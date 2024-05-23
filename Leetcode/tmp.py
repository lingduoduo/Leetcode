import collections
import functools
import heapq
from multiprocessing import heap
from typing import List
from itertools import accumulate
import operator


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        grid = [[] for i in range(n)]
        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)
        visited = [0] * n
        x = self.dfs(0, grid, hasApple, visited)
        if x == -1:
            return 0
        return x

    def dfs(self, node, grid, hasApple, visited):
        visited[node] = 1
        ct = 0
        for i in grid[node]:
            if visited[i] == 1:
                continue
            x = self.dfs(i, grid, hasApple, visited)
            if x != -1:
                ct += x
                ct += 2
        if ct > 0 or hasApple[node] == True:
            return ct
        return -1


if __name__ == "__main__":
    res = Solution().findDiagonalOrder(nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]])
    print(res)




