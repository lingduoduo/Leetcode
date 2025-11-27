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

        if n == 0 or n == 1:
            return nums

        nums = sorted(nums)

        dp = [0] * n
        max_num = 0
        max_index = 0
        child = [0] * n
        result = []

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if nums[j] % nums[i] == 0 and dp[i] < dp[j] + 1:
                    dp[i] = dp[j] + 1
                    child[i] = j

                    # To store max subset length and relative start point index
                    if max_num < dp[i]:
                        max_num = dp[i]
                        max_index = i

        # Construct output subset
        i = max_index
        for j in range(max_num):
            result.append(nums[i])
            i = child[i]

        return result
