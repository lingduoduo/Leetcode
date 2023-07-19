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


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            res = max(res, current_sum)

        return res


class Solution:
    def maxSubArray(self, nums):
        result = float("-inf")  # 初始化结果为负无穷大
        count = 0
        for i in range(len(nums)):
            count += nums[i]
            if count > result:  # 取区间累计的最大值（相当于不断确定最大子序终止位置）
                result = count
            if count <= 0:  # 相当于重置最大子序起始位置，因为遇到负数一定是拉低总和
                count = 0
        return result


if __name__ == "__main__":
    # numbers = [-2,1,-3,4,-1,2,1,-5,4]
    numbers = [-2, 1]
    result = Solution().maxSubArray(numbers)
    print(result)
