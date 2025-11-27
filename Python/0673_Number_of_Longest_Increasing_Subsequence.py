import collections
from typing import List
import bisect


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        dp = collections.defaultdict(collections.Counter)
        dp[-1][float("-inf")] = 1
        table = []
        for num in nums:
            i = bisect.bisect_left(table, num)
            if i == len(table):
                table.append(num)
            else:
                table[i] = num
            dp[i][num] += sum(dp[i - 1][j] for j in dp[i - 1] if j < num)
        return sum(dp[max(0, len(table) - 1)].values())


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        count = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    if length[j] + 1 > length[i]:
                        length[i] = length[j] + 1
                        count[i] = 0
                    if length[j] + 1 == length[i]:
                        count[i] += count[j]
        max_length = max(length)
        res = 0
        for i in range(n):
            if length[i] == max_length:
                res += count[i]
        return res
