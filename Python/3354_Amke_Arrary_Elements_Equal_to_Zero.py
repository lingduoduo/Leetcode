class Solution:
    def countValidSelections(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0
        s = sum(nums)
        left, right = 0, s
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    res += 1
                if 0 <= right - left <= 1:
                    res += 1
            else:
                left += nums[i]
                right -= nums[i]
        return res