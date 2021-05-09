class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        first = days[0]
        last = days[-1]

        days = set(days)
        dp = [0] * (1 + last)
        for i in range(first,  last + 1):
            if i in days:
                p1 = dp[i-1] if i - 1 > 0 else 0
                p7 = dp[i-7] if i - 7 > 0 else 0
                p30 = dp[i-30] if i - 30 > 0 else 0
                dp[i] = min(p1 + costs[0], p7 + costs[1],  p30 + costs[2])
            else:
                dp[i] = dp[i-1]
        return dp[-1]

