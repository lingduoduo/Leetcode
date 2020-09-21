class Solution:
    def minCut(self, s: str) -> int:
        dp = [0 for i in range(len(s)+1)]
        p = [[False for i in range(len(s))] for j in range(len(s))]
        for i in range(len(s)+1):
            dp[i] = len(s) - i
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (((j - i) < 2) or p[i+1][j-1]):
                    p[i][j] = True
                    dp[i] = min(1+dp[j+1], dp[i])
        return dp[0]-1

if __name__ == '__main__':
    result = Solution().minCut('abb')
    print(result)