from typing import List
import heapq
from collections import defaultdict


class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m = len(mat)
        n = len(mat[0])

        def dfs(i, j):
            nei = []
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n:
                    nei.append(mat[nx][ny])
                    
            if not nei or mat[i][j] > max(nei):
                return [i, j]
                
            
            for dx, dy in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
                nx, ny = i + dx, j + dy
                if 0 <= nx < m and 0 <= ny < n and mat[i][j] < mat[nx][ny]:
                    return dfs(nx, ny)
        
        return dfs(0, 0)


if __name__ == "__main__":
    res = Solution().findPeakGrid(mat = [[10,20,15],[21,30,14],[7,16,32]])
    print(res)
