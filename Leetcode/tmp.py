from typing import List
from collections import defaultdict, deque

class Solution:
    def search(self, nums: List[int], target: int) -> int:      
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1
    
if __name__ == "__main__":
   res = Solution().search(nums = [1], target = 0)
   print(res)