class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        cumsum = 0
        res = 0
        for num in gain:
            cumsum += num
            res = max(res, cumsum)
        return res
