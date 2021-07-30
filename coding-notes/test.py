class Solution:
    def cutRope(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[1] = 1
        for i in range(2, n+1):
            for j in range(1, i):
                dp[i] = max(dp[i], dp[j] * (i-j), j * (i - j))
        return dp[n]

if __name__ == '__main__':
    res = Solution().cutRope(n=10)
    print(res)
