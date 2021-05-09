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

    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        nrow = len(triangle)
        ncol = len(triangle[-1])
        f = [[float('inf')]*ncol for _ in range(nrow)]
        print(f)

        for i in range(nrow):
            for j in range(i+1):
                f[i][j] = triangle[i][j]
                print(f[i][j])
                if i==0 and j==0:
                    continue
                if j==0:
                    f[i][j] += f[i-1][j]
                elif i==j:
                    f[i][j] += f[i-1][j-1]
                else:
                    f[i][j] += min(f[i-1][j], f[i-1][j-1])
        return min(f[-1])

if __name__ == "__main__":
    ##matrix = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
    matrix = [[-1], [2, 3], [1, -1, -3]]
    result = Solution().minimumTotal(matrix)
    print(result)
