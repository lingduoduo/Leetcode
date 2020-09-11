class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        dp = triangle[-1]
        
        for i in range(len(triangle) - 2, -1, -1):
            for j in range(len(triangle[i])):
                dp[j] = min(dp[j], dp[j + 1]) + triangle[i][j]
        return dp[0]


if __name__ == "__main__":
    ###matrix = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    matrix = [[-1], [2, 3], [1, -1, -3]]
    result = Solution().minimumTotal(matrix)
    print(result)
