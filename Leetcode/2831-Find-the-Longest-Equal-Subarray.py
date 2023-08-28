class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        res = 0
        start = 0
        d = collections.Counter()
        for i in range(len(nums)):
            d[nums[i]] += 1
            res = max(res, d[nums[i]])
            if i - start + 1 - res > k:
                d[nums[start]] -= 1
                start += 1
        return res
