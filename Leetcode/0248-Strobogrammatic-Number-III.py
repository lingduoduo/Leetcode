from typing import List
from  bisect import bisect_left, bisect_right

class Solution:

    def strobogrammaticInRange(self, low: str, high: str) -> int:
        dp = dict()
        dp[0] = ['0', '1', '8']
        dp[1] = ['00', '11', '88', '69', '96']
        for i in range(2, len(high) + 1):
            dp[i] = []
            for j in dp[i - 2]:
                dp[i].append('0' + j + '0')
                dp[i].append('1' + j + '1')
                dp[i].append('8' + j + '8')
                dp[i].append('6' + j + '9')
                dp[i].append('9' + j + '6')

        nums = []
        for d in dp:
            for v in dp[d]:
                if v[0] == '0' and len(v) > 1: continue
                nums.append(int(v))
        nums.sort()
        left = bisect_left(nums, int(low))
        right = bisect_right(nums, int(high))
        return right - left

if __name__ == '__main__':
    res = Solution().strobogrammaticInRange("0", "100")
    print(res)


