from typing import List


class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        s = sum(stones)
        dp = [0] * (s + 1)
        dp[0] = 1
        for i in range(len(stones)):
            for j in range(len(dp) - 1, -1, -1):
                if j - stones[i] < 0:
                    break
                if dp[j - stones[i]]:
                    dp[j] = 1

        res = s + 1
        for psum in range(1, s + 1):
            if dp[psum] and 2 * psum - s >= 0:
                res = min(res, 2 * psum - s)
        return res


class Solution:
    def lastStoneWeightII(self, stones):
        s = sum(stones)
        target = s // 2
        dp = [0] * (target + 1)
        for stone in stones:
            for j in range(target, stone - 1, -1):
                dp[j] = max(dp[j], dp[j - stone] + stone)
        return s - 2 * dp[-1]
