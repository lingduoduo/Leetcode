class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        for left in range(n - 1, 0, -1):
            for right in range(left + 1, n + 1):
                dp[left][right] = min(i + max(dp[left][i - 1], dp[i + 1][right]) for i in range(left, right))
        
        return dp[1][n]

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(n+1)]

        def helper(left, right):
            if left >= right:
                return 0

            if dp[left][right] > 0:
                return dp[left][right]

            for i in range(left, right + 1):
                l = helper(left, i - 1)
                r = helper(i + 1, right)
                if dp[left][right] == 0:
                    dp[left][right] = i + max(l, r)
                else:
                    dp[left][right] = min(dp[left][right], i + max(l, r))
            return dp[left][right]

        return helper(1, n)

if __name__ == '__main__':
    res = Solution().getMoneyAmount(10)
    print(res)