from functools import lru_cache
from typing import List


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i, j):
            if i < 0 or j < 0 or i == len(dungeon) or j == len(dungeon[i]):
                return float("-inf")

            if i == len(dungeon) - 1 and j == len(dungeon[i]) - 1:
                return min(0, dungeon[i][j])

            return min(0, dungeon[i][j] + max(dfs(i + 1, j), dfs(i, j + 1)))

        return (-dfs(0, 0)) + 1


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        dp = dungeon

        dp[m - 1][n - 1] = max(1, 1 - dp[m - 1][n - 1])
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(1, dp[i + 1][n - 1] - dp[i][n - 1])
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(1, dp[m - 1][j + 1] - dp[m - 1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                dp[i][j] = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dp[i][j])
        return dp[0][0]


if __name__ == "__main__":
    dungeon = [[-2, -3, 3], [-5, -10, 1], [10, 30, -5]]
    ###dungeon = [[100]]
    solu = Solution()
    print(solu.calculateMinimumHP(dungeon))
