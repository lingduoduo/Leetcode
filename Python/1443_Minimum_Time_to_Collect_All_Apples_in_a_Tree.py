import collections
import heapq

from typing import List
class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        def dfs(node):
            visited[node] = 1
            res = 0
            for i in grid[node]:
                if visited[i] == 1:
                    continue
                x = dfs(i)
                if x != -1:
                    res += x
                    res += 2
            return res if res > 0 or hasApple[node] == True else -1

        grid = [[] for i in range(n)]
        for i, j in edges:
            grid[i].append(j)
            grid[j].append(i)
        visited = [0] * n
        x = dfs(0)
        if x == -1:
            return 0
        return x


if __name__ == "__main__":
    n = 7
    edges = [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]]
    hasApple = [False, False, True, False, True, True, False]
    results = Solution().minTime(n, edges, hasApple)
    print(results)
