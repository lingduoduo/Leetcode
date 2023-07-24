from typing import List
from typing import collections


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [collections.defaultdict(int) for _ in range(1 + n)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for k, v in dp[i].items():
                dp[i + 1][k - num] += v
                dp[i + 1][k + num] += v
        return dp[n][target]


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total_sum = sum(nums)  # 计算nums的总和
        if abs(target) > total_sum:
            return 0  # 此时没有方案
        if (target + total_sum) % 2 == 1:
            return 0  # 此时没有方案
        target_sum = (target + total_sum) // 2  # 目标和

        # 创建二维动态规划数组，行表示选取的元素数量，列表示累加和
        dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]

        # 初始化状态
        dp[0][0] = 1

        # 动态规划过程
        for i in range(1, len(nums) + 1):
            for j in range(target_sum + 1):
                dp[i][j] = dp[i - 1][j]  # 不选取当前元素
                if j >= nums[i - 1]:
                    dp[i][j] += dp[i - 1][j - nums[i - 1]]  # 选取当前元素

        return dp[len(nums)][target_sum]  # 返回达到目标和的方案数


if __name__ == "__main__":
    res = Solution().findTargetSumWays(nums=[1, 1, 1, 1, 1], target=3)
    print(res)
