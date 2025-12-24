class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        left = 0
        tot = 0
        for right, x in enumerate(nums):
            tot += x
            while left <= right and tot * (right - left + 1) >= k:
                tot -= nums[left]
                left += 1
            res += (right - left + 1)
        return res
    