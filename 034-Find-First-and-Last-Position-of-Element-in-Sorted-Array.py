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

        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    # nums = [-1,0,3,5,9,12]
    # nums = [-1,0,3,3,5,9,12]
    # nums = [5]
    # nums = [5,7,7,8,8,10]
    # nums = [1,2,3]
    # result = Solution().lowerBound(nums, 3)
    # result = Solution().upperBound(nums, 3)
    # result = Solution().searchRange(nums, 8)
    # result = Solution().searchRange(nums, 6)
    nums = [1, 1]
    result = Solution().lowerBound(nums, 1)
    print(result)
    result = Solution().upperBound(nums, 1)
    print(result)
    result = Solution().searchRange(nums, 1)
    print(result)
