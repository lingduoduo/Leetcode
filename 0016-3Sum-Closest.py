class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        # result = float('inf')
        # nums = sorted(nums)
        #
        # for i in range(len(nums)):
        #     j = i + 1
        #     k = len(nums) - 1
        #     while j < k:
        #         if nums[i] + nums[j] + nums[k] == target:
        #             return target
        #
        #         if abs(
        #                 (nums[i] +
        #                  nums[j] +
        #                     nums[k]) -
        #                 target) < abs(
        #                 result -
        #                 target):
        #             result = nums[i] + nums[j] + nums[k]
        #
        #         if nums[i] + nums[j] + nums[k] < target:
        #             j += 1
        #
        #         if nums[i] + nums[j] + nums[k] > target:
        #             k -= 1
        # return result
        
        nums.sort()
        print(nums)
        n = len(nums)
        res = nums[0] + nums[1] + nums[n-1]
        
        for i in range(n-2):
            if i>0 and nums[i-1]==nums[i]:
                continue
            left = i+1
            right = n-1
            while left < right:
                val = nums[i] + nums[left] + nums[right]
                if abs(val-target)<abs(res-target):
                    res = val
                if val == target:
                    return target
                elif val < target:
                    left += 1
                else:
                    right -= 1
        return res

        
if __name__ == "__main__":
    # nums = [-1, 2, 1, -4]
    # nums = [-1,-5,-3,-4,2,-2]
    nums = [0, 2, 1, -3]
    result = Solution().threeSumClosest(nums, 1)
    print(result)

