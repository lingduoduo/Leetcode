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