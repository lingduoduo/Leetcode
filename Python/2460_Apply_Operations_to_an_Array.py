from typing import List
class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                nums[i] *= 2
                nums[i + 1] = 0
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[idx], nums[i] = nums[i], nums[idx]
                idx += 1
        return nums

if __name__ == '__main__':
    res = Solution().applyOperations(nums = [1,2,2,1,1,0])
    print(res)
    res = Solution().applyOperations(nums = [0,1])
    print(res)

