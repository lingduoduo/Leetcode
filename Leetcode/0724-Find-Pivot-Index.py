from typing import List
# class Solution(object):
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums:
#             return -1
        
#         dp = [0] * (len(nums) + 1)
        
#         for i in range(len(nums)):
#             dp[i + 1] = dp[i] + nums[i]
        
#         result = -1
#         for i in range(len(nums)):
#             if dp[i] == dp[-1] - dp[i + 1]:
#                 result = i
        
#         return result
    
#     def pivotIndex(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#         if not nums: return -1
#         N = len(nums)
#         sums = [0] * (N + 1)
#         for i in range(N):
#             sums[i + 1] = sums[i] + nums[i]
#         for i in range(N):
#             if sums[i] == sums[-1] - sums[i + 1]:
#                 return i
#         return -1


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        res = -1
        
        pre = [0] * len(nums)
        pos = [0] * len(nums)
        for i in range(1, len(nums)):
            pre[i] = pre[i-1] + nums[i-1]
            pos[len(nums) - i - 1] = pos[len(nums) - i] + nums[len(nums) - i]
            print(pre)
        
        for i in range(len(nums)):
            if pre[i] == pos[i]:
                return i
        return -1

if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    res = Solution().pivotIndex(nums)
    print(res)