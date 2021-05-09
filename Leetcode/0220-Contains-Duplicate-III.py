class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if k <= 0 or t < 0: return False
        d = {}
        for i, num in enumerate(nums):
            key = num // (t + 1)
            if key in d \
               or key + 1 in d and d[key + 1] - num <= t \
               or key - 1 in d and num - d[key - 1] <= t:
               return True
            if i >= k:
                del d[nums[i-k] // (t + 1)]
            d[key] = num
        return False
