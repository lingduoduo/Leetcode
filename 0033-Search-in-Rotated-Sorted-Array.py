class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        ###start = 0
        ###end = len(nums) - 1
        
        ###while start <= end:
            
        ###    mid = (start + end) / 2
            
        ###    if nums[mid] == target:
        ###        return mid
            
        ###    if nums[mid] >= nums[start]:  ###当nums[mid]属于左边升序序列时
                
        ###        if target >= nums[start] and target < nums[mid]:
        ###            end = mid - 1
        ###        else:
        ###            start = mid + 1
            
        ###    if nums[mid] < nums[end]:  ###当nums[mid]属于右边升序序列时
                
        ###        if target > nums[mid] and target <= nums[end]:
        ###            start = mid + 1
        ###        else:
        ###            end = mid - 1
        
        ###return -1

        ###left = 0
        ###right = len(nums)-1

        ###while left<=right:
        ###    mid = left + (right-left)//2
        ###    if nums[mid]==target:
        ###        return mid
        ###    if target >= nums[0]:
        ###        if target > nums[mid] and nums[mid] >= nums[0]:
        ###            left = mid + 1
        ###        else:
        ###            right = mid - 1
        ###    else:
        ###        if nums[0]<=nums[mid] or nums[mid] < target:
        ###            left = mid + 1
        ###        else:
        ###            right = mid - 1
        ###return -1

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right-left)//2

            if nums[mid]==target:
                return mid

            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right = mid
                else:
                    left = mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left = mid + 1
                else:
                    right = mid
        return -1






