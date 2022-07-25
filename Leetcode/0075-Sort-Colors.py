class Solution(object):
    def sortColors(self, nums):
        left = 0
        right = len(nums) - 1
        curr = 0

        while curr <= right:
            if left < curr and nums[curr] == 0:
                nums[left], nums[curr] = nums[curr], nums[left]
                left += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
            else:
                curr += 1


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """ Do not return anything, modify nums in-place instead. """
        p0, p1, p2 = 0, 0, len(nums) - 1
        while p1 <= p2:
            if nums[p1] == 0:
                nums[p0], nums[p1] = nums[p1], nums[p0]
                p0 += 1
                p1 += 1
            elif nums[p1] == 2:
                nums[p1], nums[p2] = nums[p2], nums[p1]
                p2 -= 1
            else:
                p1 += 1


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    result = Solution().sortColors(nums)
    print(result)

    nums = [0, 0, 1, 0, 1, 1]
    result = Solution().sortColors(nums)
    print(result)

    nums = [1, 1, 1, 2]
    result = Solution().sortColors(nums)
    print(result)

    nums = [2, 0, 1]
    result = Solution().sortColors(nums)
    print(result)

    nums = [1, 0]
    result = Solution().sortColors(nums)
    print(result)
