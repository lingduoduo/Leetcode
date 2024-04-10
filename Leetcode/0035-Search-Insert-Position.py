class Solution(object):
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[left] == nums[mid]:
                left += 1
                right -= 1
            elif nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1
        return nums[left]

    def searchInsert(self, nums, target):
        '''
        分别处理如下四种情况
            # 目标值在数组所有元素之前  [0, -1]
            # 目标值等于数组中某一个元素  return middle;
            # 目标值插入数组中的位置 [left, right]，return  right + 1
            # 目标值在数组所有元素之后的情况 [left, right]， 因为是右闭区间，所以 return right + 1
        '''
        left, right = 0, len(nums) - 1
        while left <= right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
            else:
                return middle
        return right + 1
    
    
    def searchInsert(self, nums, target):
        '''
        分别处理如下四种情况
            # 目标值在数组所有元素之前 [0,0)
            # 目标值等于数组中某一个元素 return middle
            # 目标值插入数组中的位置 [left, right) ，return right 即可
            # 目标值在数组所有元素之后的情况 [left, right)，因为是右开区间，所以 return right
        '''
        left, right = 0, len(nums)
        while left < right:
            middle = (left + right) // 2

            if nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle
            else:
                return middle
        return right    

if __name__ == "__main__":
    nums = [1, 3, 5, 6]
    result = Solution().searchInsert(nums, 0)
    print(result)
