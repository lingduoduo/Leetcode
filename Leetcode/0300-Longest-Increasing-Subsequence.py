class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


import bisect


class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums:
            return 0

        res = []
        for i in range(len(nums)):
            print(res)
            index = bisect.bisect_left(res, nums[i])
            if len(res) == index:
                res.append(nums[i])
            else:
                res[index] = nums[i]
        return len(res)


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [1] * len(nums)
        dp[0] = 1
        for i in range(1, len(nums)):
            for j in range(0, i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


if __name__ == '__main__':
    # nums = [10,9,2,5,3,7,101,18]
    # result = Solution().lengthOfLIS(nums)
    # print(result)

    nums = [0, 1, 0, 3, 2, 3]
    result = Solution().lengthOfLIS(nums)
    print(result)
