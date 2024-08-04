class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        d = collections.Counter(nums)

        res = 0

        if k == 0:
            for v in d.values():
                if v > 1:
                    res += 1
        else:
            for num in d:
                if num - k in d:
                    res += 1
        return res
