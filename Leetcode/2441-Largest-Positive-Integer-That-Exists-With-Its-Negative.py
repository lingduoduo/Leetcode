class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numset = set(nums)
        res = -1
        for num in nums:
            if num > 0 and -num in numset:
                res = max(res, num)
        return res
