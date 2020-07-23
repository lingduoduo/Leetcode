class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # if nums is None:
        #     return -1
        #
        # n = len(nums)
        # i = 0
        # j = 0
        # for j in range(0, n):
        #     if nums[j] != val:
        #         nums[i] = nums[j]
        #         i = i + 1
        # return i
        
        


if __name__ == "__main__":
    numbers = [3, 2, 2, 3]
    results = Solution().removeElement(numbers, 3)
    print(results)
