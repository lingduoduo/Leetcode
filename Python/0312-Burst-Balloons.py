from typing import List


class Solution(object):
    def maxCoins(self, nums):
        n = len(nums)
        nums = [1] + nums + [1]
        c = [[0] * (n + 2) for _ in range(n + 2)]
        return self.dfs(nums, c, 1, n)

    def dfs(self, nums, c, i, j):
        if i > j:
            return 0
        if c[i][j] > 0:
            return c[i][j]
        if i == j:
            return nums[i - 1] * nums[i] * nums[i + 1]
        res = 0
        for k in range(i, j + 1):
            res = max(
                res,
                self.dfs(nums, c, i, k - 1)
                + nums[i - 1] * nums[k] * nums[j + 1]
                + self.dfs(nums, c, k + 1, j),
            )
        c[i][j] = res
        return c[i][j]


class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]
        for i in range(n - 2, -1, -1):
            for j in range(i + 2, n):
                for k in range(i + 1, j):
                    dp[i][j] = max(
                        dp[i][j], nums[i] * nums[k] * nums[j] + dp[i][k] + dp[k][j]
                    )
        return dp[0][n - 1]


if __name__ == "__main__":
    nums = [3, 1, 5, 8]
    res = Solution().maxCoins(nums)
    print(res)
