from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        nums.sort()
        dp = [[0, i] for i in range(len(nums))]
        idx = max_len = 0
        for i, num in enumerate(nums):
            tmp = 0
            for k in range(i):
                if nums[i] % nums[k] == 0:
                    if tmp < dp[k][0]:
                        tmp = dp[k][0]
                        dp[i][1] = k
            dp[i][0] = tmp + 1
            if dp[i][0] > max_len:
                max_len = dp[i][0]
                idx = i

        res = [nums[idx]]
        while idx != dp[idx][1]:
            idx = dp[idx][1]
            res.append(nums[idx])
        return res[::-1]


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        nums.sort()
        dp = [1] * n
        pre = [-1] * n
        best_len = 1
        best_end = 0
        for i in range(n):
            for j in range(i - 1, -1, -1):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pre[i] = j

            if dp[i] > best_len:
                best_len = dp[i]
                best_end = i

        res = []
        idx = best_end
        while idx != -1:
            res.append(nums[idx])
            idx = pre[idx]
        res.reverse()
        return res
