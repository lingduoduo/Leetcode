class Solution:
    def getMost(self, matrix) -> int:
        if not matrix:
            return 0 

        n = len(matrix)
        dp = [0] * n
        for i in range(n):
            dp[0] += matrix[i][0]
            for j in range(1, n):
                dp[j] = max(dp[j], dp[j-1]) + matrix[i][j]
        return dp[n-1]

if __name__ == '__main__':
    matrix = [[1, 10, 3, 8], [12, 2, 9, 6], [5, 7, 4, 11], [3, 7, 16, 5]]
    res = Solution().getMost(matrix=matrix)
    print(res)

# ```java
# public int getMost(int[][] values) {
#     if (values == null || values.length == 0 || values[0].length == 0)
#         return 0;
#     int n = values[0].length;
#     int[] dp = new int[n];
#     for (int[] value : values) {
#         dp[0] += value[0];
#         for (int i = 1; i < n; i++)
#             dp[i] = Math.max(dp[i], dp[i - 1]) + value[i];
#     }
#     return dp[n - 1];
# }
# ```
