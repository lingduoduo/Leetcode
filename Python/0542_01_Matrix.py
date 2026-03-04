from typing import List
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        que = deque([])
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    que.append((i, j))
                else:
                    mat[i][j] = float("inf")
                    
        while que:
            for _ in range(len(que)):
                i, j = que.popleft()
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < m and 0 <= ny < n and mat[nx][ny] > mat[i][j] + 1:
                        mat[nx][ny] = mat[i][j] + 1
                        que.append((nx, ny))
        return mat


if __name__ == "__main__":
    # matrix = [[0,0,0],[0,1,0],[0,0,0]]
    # res = Solution().updateMatrix(matrix)
    # print(res)

    matrix = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    res = Solution().updateMatrix(matrix)
    print(res)
