from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        n = len(nums)
        return max(self.rob_sub(nums[0 : n - 1]), self.rob_sub(nums[1:n]))

    def rob_sub(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return
            max(nums[0], nums[1])
        n = len(nums)
        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[-1]


class Solution:
    def _rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for i in range(len(nums)):
            dp0, dp1 = dp1, max(dp0 + nums[i], dp1)
        return dp1

    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        return max(self._rob(nums[:-1]), self._rob(nums[1:]))


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        odds = self.helper(nums[:-1])
        evens = self.helper(nums[1:])
        return max(odds, evens)

    def helper(self, vals: List[int]) -> int:
        dp = [0] * (len(vals) + 1)
        for i, num in enumerate(vals):
            if i == 0:
                dp[i + 1] = vals[i]
            else:
                dp[i + 1] = max(dp[i], dp[i - 1] + vals[i])
        return dp[-1]


if __name__ == "__main__":
    res = Solution().rob([1, 2, 3])
    print(res)
