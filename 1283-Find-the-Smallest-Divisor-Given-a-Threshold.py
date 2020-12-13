class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums) + 1
        res = 0
        while left < right:
            mid = left + (right - left)//2
            tot = sum((x-1)//mid + 1 for x in nums)
            if tot  <= threshold:
                res = mid
                right = mid 
            else:
                left = mid + 1
        return res
        