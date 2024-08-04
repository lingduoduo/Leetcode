class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        Input:

                1 0 1 0 0
                1 0 1 1 1
                1 1 1 1 1
                1 0 0 1 0

                Output: 4
        """

        # if not matrix:
        #     return 0
        # n = len(matrix)
        # p = len(matrix[0])
        # dp = [[0] * p for _ in range(n)]

        # res = 0

        # for i in range(n):
        #     dp[i][0] = int(matrix[i][0])
        #     res = max(res, dp[i][0] ** 2)
        # for j in range(p):
        #     dp[0][j] = int(matrix[0][j])
        #     res = max(res, dp[0][j] ** 2)

        # for i in range(1, n):
        #     for j in range(1, p):
        #         if int(matrix[i][j]) == 1:
        #             dp[i][j] = min(dp[i - 1][j], dp[i][j - 1],
        #                            dp[i - 1][j - 1]) + 1
        #         res = max(res, dp[i][j] ** 2)
        # return res


class Solution:
    def maximalSquare(self, matrix) -> int:
        if not matrix:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        dp = [[0] * n for _ in range(m)]

        res = 0

        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            res = max(res, dp[i][0])

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            res = max(res, dp[0][j])

        for i in range(1, m):
            for j in range(1, n):
                if int(matrix[i][j]) == 1:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                res = max(res, dp[i][j] ** 2)

        return res


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    result = Solution().maximalSquare(matrix)
    print(result)

    matrix = [["1"]]
    result = Solution().maximalSquare(matrix)
    print(result)
