# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         result = [1] * len(nums)
#         prod = 1
#         for i in range(1, len(nums)):
#             prod *= nums[i - 1]
#             result[i] *= prod
        
#         prod = 1
#         for i in range(len(nums) - 2, -1, -1):
#             prod *= nums[i + 1]
#             result[i] *= prod
        
#         return result


class Solution(object):
    def productExceptSelf(self, nums):
        fromLeft = []
        cum = 1
        for num in nums:
            cum *= num
            fromLeft.append(cum)
        cum = 1
        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                fromLeft[i] = fromLeft[i-1]
                cum *= nums[i]
                continue
            elif i == 0:
                fromLeft[i] = cum
            else:
                fromLeft[i] = fromLeft[i-1]*cum
                cum *= nums[i]
        return fromLeft

if __name__ == '__main__':
    nums = [1,2,3,4]
    results = Solution().productExceptSelf(nums)
    print(results)