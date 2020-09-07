class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cumsum = 0
        d = {}
        d[0] = -1
        res = 0
        for i, num in enumerate(nums):
            if num == 0:
                cumsum -= 1
            else:
                cumsum += 1
            if cumsum in d:
                res = max(res, i-d[cumsum])
            else:
                d[cumsum]=i
        return res
        
