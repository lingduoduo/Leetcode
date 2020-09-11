class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ###First try
        ###if target < nums[0]:
        ###    return 0
        
        ###for i in range(len(nums)):
        ###  if target <= nums[i]:
        ###      return i
        ###return len(nums)
        
        #######Second try
        ###left=0
        ###right=len(nums)-1
        
        ###while left<=right:
        ###    mid=left+(right-left)/2
        
        ###    if nums[left]==target:
        ###        return left
        ###    elif nums[right]==target:
        ###        return right
        ###    elif nums[mid]==target:
        ###        return mid
        
        ###    if nums[mid]<target:
        ###        left=mid+1
        ###    else:
        ###        right=mid-1
        
        ###return left
        
        ###Second Try
        ###if not nums:
        ###    return 0
        #
        ###left = 0
        ###right = len(nums)
        #
        ###while left < right:
        ###    mid = left + (right - left) // 2
        ###    if nums[mid] == target:
        ###        return mid
        ###    elif nums[mid] < target:
        ###        left = mid + 1
        ###    else:
        ###        right = mid
        ###return left
        
        ###for i in range(len(nums)):
        ###    if nums[i] == target:
        ###        return i
        ###    elif nums[i]<target and target<nums[i+1]:
        ###        return i
        ###return len(nums)

        left, right = 0, len(nums)
        while left < right:
            mid = left + (right-left)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]<target:
                left = mid+1
            else:
                right = mid
                
        return left



if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    result = Solution().searchInsert(nums, 0)
    print(result)
