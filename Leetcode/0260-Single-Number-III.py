class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        diff = 0
        for num in nums:
            diff ^= num 
        diff &= -diff

        res1 = 0 
        res2 = 0
        for num in nums:
            if num & diff == 0:
                res1 ^= num 
            else:
                res2 ^= num
        return sorted([res1, res2])