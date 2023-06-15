class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * (len(nums) + 1)
        dp[0] = 0
        dp[1] = nums[0]
        for i in range(1, len(nums)):
            dp[1 + i] = max(dp[i - 1] + nums[i], dp[i])

        return dp[len(nums)]


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp0, dp1 = 0, 0
        for num in nums:
            dp0, dp1 = dp1, max(dp0 + num, dp1)
        return dp1


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp0 = dp1 = 0
        for num in nums:
            dp0, dp1 = dp1, max(dp1, dp0 + num)
        return dp1


class Solution:
    def __init__(self):
        self.memo = {}

    def rob(self, nums: List[int]) -> int:
        self.memo = {}

        return self.robFrom(0, nums)

    def robFrom(self, i, nums):
        # No more houses left to examine.
        if i >= len(nums):
            return 0

        # Return cached value.
        if i in self.memo:
            return self.memo[i]

        # Recursive relation evaluation to get the optimal answer.
        ans = max(self.robFrom(i + 1, nums), self.robFrom(i + 2, nums) + nums[i])

        # Cache for future use.
        self.memo[i] = ans
        return ans


class Solution:
    def rob(self, nums: List[int]) -> int:
        @lru_cache(maxsize=None)
        def robFrom(i):
            # No more houses left to examine.
            if i >= len(nums):
                return 0

            # Recursive relation evaluation to get the optimal answer.
            return max(robFrom(i + 1), robFrom(i + 2) + nums[i])

        return robFrom(0)
