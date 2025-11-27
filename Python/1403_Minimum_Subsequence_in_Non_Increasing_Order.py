class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        res = [0] * len(nums)
        for i in range(len(nums)):
            if i == 0:
                res[i] = nums[i]
            else:
                res[i] = res[i - 1] + nums[i]

        j = len(nums) - 1
        cum = 0
        while j > 0:
            if j == len(nums) - 1:
                cum = nums[j]
            else:
                cum += nums[j]
            if cum > res[j - 1]:
                return nums[j:][::-1]
            j -= 1
        return nums[::-1]
