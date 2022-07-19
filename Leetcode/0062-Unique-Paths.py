class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if i == 1 and j == 1:
                    d[i][j] = 1
                else:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]
        return d[m][n]


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                dp[j] += dp[j - 1]
        return dp[-1]


if __name__ == "__main__":
    result = Solution().uniquePaths(3, 7)
    print(result)
