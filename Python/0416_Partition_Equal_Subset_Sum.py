from typing import List


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
        total = sum(nums)
        if total % 2 != 0:
            return False

        target = total // 2
        dp = [[False] * (1 + target) for _ in range(1 + len(nums))]

        for i in range(len(nums) + 1):
            dp[i][0] = True

        for i in range(1, len(nums) + 1):
            for j in range(1, target + 1):
                if j < nums[i - 1]:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        return dp[-1][-1]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        dp = [False] * (target_sum + 1)
        dp[0] = True

        for num in nums:
            # 从target_sum逆序迭代到num，步长为-1
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        return dp[target_sum]


if __name__ == "__main__":
    nums = [1, 5, 11, 5]
    res = Solution().canPartition(nums)
    print(res)
