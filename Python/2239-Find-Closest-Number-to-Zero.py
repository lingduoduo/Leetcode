from typing import List

class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        res = min(abs(x) for x in nums)
        return res if res in nums else -res