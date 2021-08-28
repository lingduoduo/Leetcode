# class Solution(object):
#     def moveZeroes(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: void Do not return anything, modify nums in-place instead.
#         """
#         ###for i in range(len(nums) - 1, -1, -1):
#         ###    if nums[i] == 0:
#         ###        nums.pop(i)
#         ###        nums.append(0)
        
#         pos = 0
#         for i in range(len(nums)):
#             if nums[i]:
#                 nums[pos] = nums[i]
#                 pos += 1
        
#         for i in range(pos, len(nums)):
#             nums[i] = 0
    
        

class Solution(object):
    def moveZeroes(self, nums):
        i = 0 
        j = len(nums) - 1
        while i < j:
            while nums[i] != 0 and i < j:
                i += 1
            while nums[j] == 0 and i < j:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        return nums


if __name__ == '__main__':
    res = Solution().moveZeroes(nums=[0, 1, 0, 3, 12])
    print(res)