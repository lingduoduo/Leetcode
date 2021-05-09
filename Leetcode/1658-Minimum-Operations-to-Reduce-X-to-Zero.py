class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        if target == 0:
            return len(nums)
        if target < 0:
            return -1
        l, r, partsum = 0, 0, 0
        res = -1
        while r < len(nums):
            partsum += nums[r]
            r += 1
            while partsum >= target:
                if partsum == target:
                    res = max(res, r-l)
                partsum -= nums[l]
                l += 1
        return -1 if res == -1 else len(nums) - res


