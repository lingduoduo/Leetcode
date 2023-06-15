class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        n = len(nums)
        tot = sum(nums)
        dp = [collections.defaultdict(int) for _ in range(1 + n)]
        dp[0][0] = 1
        for i, num in enumerate(nums):
            for k, v in dp[i].items():
                dp[i + 1][k - num] += v
                dp[i + 1][k + num] += v
        return dp[n][S]
