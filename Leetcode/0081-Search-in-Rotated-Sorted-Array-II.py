class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            while left < right and nums[left] == nums[right]:
                left += 1
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                elif nums[left] <= nums[mid] < target:
                    left = mid + 1
                elif target <= nums[left] <= nums[mid]:
                    left = mid + 1
            elif nums[mid] <= nums[right]:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                elif target < nums[mid] <= nums[right]:
                    right = mid - 1
                elif nums[mid] <= nums[right] <= target:
                    right = mid - 1
        return False
