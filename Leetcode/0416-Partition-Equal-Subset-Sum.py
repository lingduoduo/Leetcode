from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2 != 0:
            return False

        dp = [0] * (s + 1)
        dp[0] = 1
        for num in nums:
            for i in range(s, -1, -1):
                if dp[i]:
                    dp[i + num] = 1

            if dp[s // 2]:
                return True

        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        s = sum(nums)
        if s % 2 == 1:
            return False

        dp = [True] + [False] * s
        for idx, num in enumerate(nums):
            for j in range(s // 2, num - 1, -1):
                dp[j] |= dp[j - num]
            if dp[s // 2]:
                return True
        return False


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
        subset_sum = total_sum // 2
        n = len(nums)

        # construct a dp table of size (n+1) x (subset_sum + 1)
        dp = [[False] * (subset_sum + 1) for _ in range(n + 1)]
        dp[0][0] = True
        for i in range(1, n + 1):
            curr = nums[i - 1]
            for j in range(subset_sum + 1):
                if j < curr:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - curr]
        return dp[n][subset_sum]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    res = Solution().canPartition(nums)
    print(res)
