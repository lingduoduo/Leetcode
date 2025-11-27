from typing import List


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


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 0:  # 如果没有房屋，返回0
            return 0
        if len(nums) == 1:  # 如果只有一个房屋，返回其金额
            return nums[0]

        # 创建一个动态规划数组，用于存储最大金额
        dp = [0] * len(nums)
        dp[0] = nums[0]  # 将dp的第一个元素设置为第一个房屋的金额
        dp[1] = max(nums[0], nums[1])  # 将dp的第二个元素设置为第一二个房屋中的金额较大者

        # 遍历剩余的房屋
        for i in range(2, len(nums)):
            # 对于每个房屋，选择抢劫当前房屋和抢劫前一个房屋的最大金额
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])

        return dp[-1]  # 返回最后一个房屋中可抢劫的最大金额


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
