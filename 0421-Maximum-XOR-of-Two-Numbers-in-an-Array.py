class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(31, -1, -1):
            res <<= 1
            pre = set(n >> i for n in nums)
            res += any(res ^ 1 ^ p in pre for p in pre)
        return res
        