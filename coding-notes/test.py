class Solution():
    def diceSum(self, n: int):
        face = 6 
        pointNum = face * n 
        dp = [[0] * ( 1 + pointNum)] *(1 + n)

        for i in range(1, face + 1):
            dp[1][i] = 1 

        for i in range(2, 1 + n):
            for j in range(i, pointNum + 1):
                for k in range(1, face + 1):
                    if j - k >= 0:
                        dp[i][j] += dp[i - 1][j - k] + 1
        totalNum = face ** n 

        res = []
        for i in range(n, pointNum + 1):
            res.append(dp[n][i] / totalNum)
        return res

if __name__ == '__main__':
    res = Solution().diceSum(2)
    print(res)
