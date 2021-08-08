class Solution:
    def numDecodings(self, s: str) -> int:
        strs = list(str(s))
        if len(strs) == 0:
            return 0

        dp = [0] * (1 + len(strs))
        dp[0] = 1
        dp[1] = 0 if str(strs[0]) == '0' else 1
        
        for i in range(2, len(strs) + 1):
            print(dp)
            one = strs[i-1: i]
            if one != "0":
                dp[i] += dp[i-1]

            two = strs[i-2: i-1]
            if two == '0':
                continue
            else:
                if int(''.join(strs[i-2: i])) <= 26:
                    dp[i] += dp[i-2]

        return dp[len(strs)]

if __name__ == '__main__':
    res = Solution().numDecodings(12258)
    print(res)


