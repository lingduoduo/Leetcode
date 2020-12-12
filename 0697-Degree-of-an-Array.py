class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = collections.defaultdict(list)
        degree = 0
        for idx, num in enumerate(nums):
            d[num] += [idx]
            degree = max(degree, len(d[num]))
        res = len(nums)
        for k, v in d.items():
            if len(d[k]) == degree:
                res = min(res, max(d[k]) - min(d[k]) + 1)
        return res
                