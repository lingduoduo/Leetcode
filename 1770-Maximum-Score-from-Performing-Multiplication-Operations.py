from typing import List
class Solution:
    def maximumScore(self, nums: List[int], multipliers: List[int]) -> int:
        res = float("-inf")
        n = len(nums)
        dp = [[0]*n for _ in range(n)]

        def dfs(i, j):
        	k = n -  (j - i + 1)
        	if k == len(multipliers):
        		return 0
        	return max(
        		dfs(i+1, j) + nums[i]*multipliers[k], 
        		dfs(i, j-1) + nums[j]*multipliers[k]
        		)
        
        return dfs(0, n-1)


if __name__ == '__main__':
	nums = [1,2,3]
	multipliers = [3,2,1]
	res = Solution().maximumScore(nums, multipliers)
	print(res)
