class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        if len(nums) < 3:
            return 0
        res = 0
        for i in range(len(nums) - 2):
            idx1 = bisect_left(nums, nums[i] + diff)
            idx2 = bisect_left(nums, nums[i] + 2 * diff)
            if idx1 == len(nums) or idx2 == len(nums) or nums[idx1] != nums[i] + diff or nums[idx2] != nums[
                i] + 2 * diff:
                continue
            else:
                res += 1
        return res
