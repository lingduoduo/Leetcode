# class Solution(object):
#     def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # if nums is None:
        #    return -1
        
        # n = len(nums)
        # i = 0
        # j = 0
        # for j in range(0, n):
        #    if nums[j] != val:
        #        nums[i] = nums[j]
        #        i = i + 1
        # return i


class Solution(object):
    def removeElement(self, nums, val):
        if not nums:
            return 0
        
        if nums == [val]:
            return 0
        
        left = 0
        right = len(nums) - 1
        
        while left < right:
            if nums[left] != val:
                left += 1
                continue
            else:
                while left < right and nums[right] == val:
                    right -= 1
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                left += 1
        return [num != val for num in nums].count(True)

                    
if __name__ == "__main__":
    # numbers = [3, 2, 2, 3]
    nums = [3, 4, 5]
    results = Solution().removeElement(nums, 3)
    print(results)
