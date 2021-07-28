from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return None
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left)//2
            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

if __name__ == '__main__':
    res = Solution().findMin(nums=[3,4,5,1,2])
    print(res)
