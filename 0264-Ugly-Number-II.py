class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <0: return 0

        dp = [1]*n

        idx2, idx3, idx5 = 0, 0, 0

        for i in range(1, n):
            dp[i] = min(2*dp[idx2], 3*dp[idx3], 5*dp[idx5])
            if dp[i] == 2*dp[idx2]:
                idx2 += 1
            if dp[i] == 3*dp[idx3]:
                idx3 += 1
            if dp[i] == 5*dp[idx5]:
                idx5 += 1
        return dp[-1]

import heapq
class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n <0: return 0

        res = []
        nums = [1]
        while len(res) < n:
            num = heapq.heappop(nums)
            res.append(num)
            for i in [2, 3, 5]:
                if num*i not in nums:
                    heapq.heappush(nums, num*i)

        return res[n-1]

if __name__ == '__main__':
    n = 10
    results = Solution().nthUglyNumber(n)
    print(results)

