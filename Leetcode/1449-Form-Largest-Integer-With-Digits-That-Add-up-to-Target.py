class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        dp = [0] + [-1] * (target)
        for t in range(1, target + 1):
            for i, c in enumerate(cost):
                if t - c >= 0:
                    dp[t] = max(dp[t], dp[t - c] * 10 + i + 1)
        return str(max(dp[target], 0))
