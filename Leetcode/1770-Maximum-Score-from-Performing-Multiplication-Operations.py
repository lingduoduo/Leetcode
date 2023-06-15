from typing import List


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        res = float("-inf")
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        def dfs(i, j):
            k = n - (j - i + 1)
            if k == len(multipliers):
                return 0
            return max(
                dfs(i + 1, j) + nums[i] * multipliers[k],
                dfs(i, j - 1) + nums[j] * multipliers[k],
            )

        return dfs(0, n - 1)


class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        # Number of Operations
        m = len(multipliers)

        # For Right Pointer
        n = len(nums)

        dp = [[0] * (m + 1) for _ in range(m + 1)]

        for op in range(m - 1, -1, -1):
            for left in range(op, -1, -1):
                dp[op][left] = max(
                    multipliers[op] * nums[left] + dp[op + 1][left + 1],
                    multipliers[op] * nums[n - 1 - (op - left)] + dp[op + 1][left],
                )

        return dp[0][0]


if __name__ == "__main__":
    nums = [1, 2, 3]
    multipliers = [3, 2, 1]
    res = Solution().maximumScore(nums, multipliers)
    print(res)
