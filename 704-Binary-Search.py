class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        left = 0
        right = len(nums)-1

        while left<=right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return -1

if __name__=="__main__":
    nums = [-1,0,3,5,9,12]
    nums = [-1,0,3,5,9,12]
    # nums = [5]
    result = Solution().search(nums, 2)
    print(result)
