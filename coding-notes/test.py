class Solution:
    def getUglyNumber_Solution(self, n) -> int:
        if n <= 6:
            return n 
        i, j, k = 0, 0, 0 
        dp = [0] * n 
        dp[0] = 1
        for idx in range(1, n):
            next2 = dp[i] * 2
            next3 = dp[j] * 3
            next5 = dp[k] * 5
            dp[idx] = min(next2, next3, next5)
            if next2 == dp[idx]:
                i += 1
            elif next3 == dp[idx]:
                j += 1
            else:
                k += 1
        return dp[-1]

if __name__ == '__main__':
    res = Solution().getUglyNumber_Solution(n=7)
    print(res)


