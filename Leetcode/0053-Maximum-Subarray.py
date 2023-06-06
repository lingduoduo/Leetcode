from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if max(nums) < 0:
            return max(nums)

        dp = [0] * (len(nums))
        dp[0] = max(dp[0], nums[0])

        for i in range(1, len(nums)):
            dp[i] = max(0, dp[i - 1] + nums[i])
        print(dp)
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        res = float("-inf")
        for num in nums:
            if pre > 0:
                res = max(res, pre + num)
                pre += num
            else:
                res = max(res, num)
                pre = num
        return res


if __name__ == "__main__":
    # numbers = [-2,1,-3,4,-1,2,1,-5,4]
    numbers = [-2, 1]
    result = Solution().maxSubArray(numbers)
    print(result)
