from collections import defaultdict, deque
from typing import List
import math
import heapq

class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        que = deque([])

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j))
                if mat[i][j] == 1:
                    mat[i][j] = float("inf")

        while que:
            for i in range(len(que)):
                x, y = que.popleft()
                for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] > mat[x][y] + 1:
                        mat[nx][ny] == mat[nx][ny] + 1
                        que.append((nx, ny))
        return mat


if __name__ == "__main__":
    res = Solution().updateMatrix(mat = [[0,0,0],[0,1,0],[0,0,0]])
    print(res)
