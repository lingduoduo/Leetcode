class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]


if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    result = Solution().searchInsert(nums, 0)
    print(result)
