class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
    	n = len(nums)
    	tot = sum(nums)
    	dp = [[0] * (2 * tot + 1) for _ in (n+1)]

    	dp[0][tot] = 1
    	for i in range(n):
    		for j in range(nums[i], tot-nums[i]):
    			if dp[i][j]:
    				dp[i + 1][nums[i] + j] += dp[i][j]
    				dp[i + 1][nums[i] - j] += dp[i][j]
