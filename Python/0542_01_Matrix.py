from typing import List
import collections


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        dist = [[float("inf")] * n for _ in range(m)]
        q = collections.deque()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dist[i][j] = 0
                    q.append((i, j))
        dirs = [[0, 1], [0, -1], [-1, 0], [1, 0]]
        while q:
            curr = q.popleft()
            for d in dirs:
                x = curr[0] + d[0]
                y = curr[1] + d[1]
                if x >= 0 and x < m and y >= 0 and y < n and matrix[x][y] == 1:
                    if dist[x][y] > dist[curr[0]][curr[1]] + 1:
                        dist[x][y] = dist[curr[0]][curr[1]] + 1
                        q.append((x, y))
        return dist


if __name__ == "__main__":
    # matrix = [[0,0,0],[0,1,0],[0,0,0]]
    # res = Solution().updateMatrix(matrix)
    # print(res)

    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = Solution().updateMatrix(matrix)
    print(res)
