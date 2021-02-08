from typing  import List

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        if len(nums) <= 2:
            return '/'.join(nums)
        return '{}/({})'.format(nums[0], '/'.join(nums[1:]))

if __name__ == '__main__':
	nums = [2,  1000,100,10]
	res = Solution().optimalDivision(nums)
	print(res)