from typing import List
# class Solution:
#     def findErrorNums(self, nums):
#         nums.sort()
#         res = []
#         for i in range(1, len(nums)+1):
#             if i not in nums:
#             	res.append(i)
#             if i <len(nums) and nums[i] == nums[i-1]:
#             	res.append(nums[i])
#         return res

# class Solution:
#     def findErrorNums(self, nums: List[int]) -> List[int]:
#          hashs = [0] * len(nums)

#         for i in range(len(nums)):
#             hashs[nums[i] - 1] += 1
#         return [hashs.index(2) + 1, hashs.index(0) + 1]

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            while nums[i] != i + 1:
                if nums[i] == nums[nums[i] - 1]:
                    break
                else:
                    j = nums[i] - 1
                    nums[i], nums[j] = nums[j], nums[i]
        res = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                res.extend([nums[i], i + 1])
        return res

if __name__ == '__main__':
	nums = [1,2,2,4]
	# nums = [3,2,2]
	# nums = [3,2,3,4,6,5]
	# nums = [1, 1]
	# nums = [2, 2]
	results = Solution().findErrorNums(nums)
	print(results)

