from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]

        # find first position >= target
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
                
        first = left
        if first == n or nums[first] != target:
            return [-1, -1]

        # find first position > target
        left, right = 0, n
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        last = left - 1
        return [first, last]
    

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums, target):
            left, right = 0, len(nums)
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left
        
        left = lower_bound(nums, target)
        right = lower_bound(nums, target + 1) - 1
        if left <= right:
            return [left, right]
        return [-1, -1]


if __name__ == "__main__":
    ###nums = [-1,0,3,5,9,12]
    ###nums = [-1,0,3,3,5,9,12]
    ###nums = [5]
    ###nums = [5,7,7,8,8,10]
    ###nums = [1,2,3]
    ###result = Solution().lowerBound(nums, 3)
    ###result = Solution().upperBound(nums, 3)
    ###result = Solution().searchRange(nums, 8)
    ###result = Solution().searchRange(nums, 6)

    ###nums = [5,7,7,8,8,10]
    target = 8
    nums = [5, 7, 7, 8, 8, 10]
    ###target = 6
    result = Solution().searchRange(nums, target)
    print(result)
    ###result = Solution().lowerBound(nums, 1)
    ###print(result)
    ###result = Solution().upperBound(nums, 1)
    ###print(result)
    ###result = Solution().searchRange(nums, 1)
    ###print(result)
