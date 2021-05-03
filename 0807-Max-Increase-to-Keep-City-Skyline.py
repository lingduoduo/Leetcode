from typing import List
class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        rows = [0] * len(grid)
        cols = [0] * len(grid[0])

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                rows[i] = max(rows[i], grid[i][j])
                cols[j] = max(cols[j], grid[i][j])

        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res += min(rows[i], cols[j]) - grid[i][j]
        return res


if __name__ == '__main__':
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    res = Solution().maxIncreaseKeepingSkyline(grid)
    print(res)