from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        res = 0
        visited = [[-1] * n for _ in range(m)]
        def dfs(m, n, i, j):
            if visited[i][j] != -1:
                return visited[i][j]
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            res = 1
            for direction in directions:
                x, y = i + direction[0], j + direction[1]
                if x < 0 or x >= m or y < 0 or y >= n or matrix[x][y] <= matrix[i][j]:
                    continue
                path = 1 + dfs(m, n, x, y)
                res = max(res, path)
            visited[i][j] = res
            return visited[i][j]

        for i in range(m):
            for j in range(n):
                path = dfs(m, n, i, j)
                res = max(res, path)
        return res

if __name__ == '__main__':
    res = Solution().longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]])
    print(res)