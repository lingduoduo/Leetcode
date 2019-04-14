class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        Input: [2,0,2,1,1,0]
		Output: [0,0,1,1,2,2]
        """
        if not nums:
            return None

        # i =0
        # while nums[i] != 0 and i<len(nums)-1:
        #     i += 1
        # if i<len(nums):
        #     nums[0], nums[i] = nums[i], nums[0]
        # i = 0
        #
        # print(nums)
        #
        # k = len(nums)-1
        # while nums[k] != 2 and k>0:
        #     k -= 1
        # if k>=0:
        #     nums[len(nums)-1], nums[k] = nums[k], nums[len(nums)-1]
        # k = len(nums) - 1
        #
        # print(nums)

        i = 0
        j = 0
        k = len(nums)-1
        while j<=k:
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j += 1
            elif nums[j] == 2:
                nums[k], nums[j] = nums[j], nums[k]
                k -= 1
            else:
                j += 1
        return nums

if __name__ == '__main__':
    nums = [2,0,2,1,1,0]
    result = Solution().sortColors(nums)
    print(result)

    nums = [0,0,1,0,1,1]
    result = Solution().sortColors(nums)
    print(result)

    nums = [1,1,1,2]
    result = Solution().sortColors(nums)
    print(result)

    nums = [2,0,1]
    result = Solution().sortColors(nums)
    print(result)

    nums = [1,0]
    result = Solution().sortColors(nums)
    print(result)

