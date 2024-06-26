from typing import List


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        lower = self.lowerBound(nums, target)
        upper = self.upperBound(nums, target)

        if lower == upper:
            return [-1, -1]
        return [lower, upper - 1]

    def lowerBound(self, nums, target):
        """
        return index such that target<=nums[index]
        """
        if not nums:
            return -1

        left = 0
        right = len(nums)

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def upperBound(self, nums, target):
        """
        return index such that target<nums[index]
        """
        if not nums:
            return -1

        left = 0
        right = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

        ###Second Try
        if not nums:
            return [-1, -1]

        if target not in nums:
            return [-1, -1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        if target not in nums:
            return [-1, -1]

        left1, right1 = 0, len(nums)
        while left1 < right1:
            mid1 = left1 + (right1 - left1) // 2
            if nums[mid1] < target:
                left1 = mid1 + 1
            else:
                right1 = mid1

        left2, right2 = 0, len(nums)
        while left2 < right2:
            mid2 = left2 + (right2 - left2) // 2
            if nums[mid2] <= target:
                left2 = mid2 + 1
            else:
                right2 = mid2

        if left1 == left2:
            return [-1, -1]
        return [left1, left2 - 1]


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.lower_bound(nums, target)
        right = self.higher_bound(nums, target)
        if left == right:
            return [-1, -1]
        return [left, right - 1]

    def lower_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

    def higher_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


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
