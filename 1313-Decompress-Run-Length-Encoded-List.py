class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        i = 0
        j = 1
        res = []
        while j < len(nums):
            res.extend([nums[j]] * nums[i])
            i += 2
            j += 2
        return res
            