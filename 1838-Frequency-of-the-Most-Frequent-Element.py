from typing import List
class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()

        count = 0
        j = 0
        res = 1
        for i in range(len(nums)):
        	count += (i - j) * (nums[i] - nums[i-1])
        	while count > k:
        		count -= nums[i] - nums[j]
        		j += 1
        	res = max(res,  i - j + 1)
        return res

if __name__ == '__main__':
	nums = [1,2,4]
	k = 5
	res = Solution().maxFrequency(nums, k)
	print(res)

