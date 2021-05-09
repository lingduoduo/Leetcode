class Solution:
    def arraySign(self, nums: List[int]) -> int:
        signs = 0
        for num in nums:
            if num < 0:
                signs += 1
            if num == 0:
                return 0
        if signs % 2 == 0:
            return 1
        else:
            return -1
            