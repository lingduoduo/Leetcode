class Solution:
    def maximumSwap(self, num: int) -> int:
        nums = list(str(num))

        left = 0
        right = 0

        max_idx = len(nums) - 1

        for idx in reversed(range(len(nums))):
            if nums[idx] > nums[max_idx]:
                max_idx = idx
            elif nums[idx] < nums[max_idx]:
                left = idx
                right = max_idx
        nums[left], nums[right] = nums[right], nums[left]
        return int(''.join(nums))
   