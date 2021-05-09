class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
    	n = len(nums)
    	dp = [0]*(n+1)

    	d = {}
    	d[0] = 0

    	curr = 0

    	for i in range(1, n+1):
    		curr += nums[i-1]

    		if curr - target in d:
    			dp[i] = 1 + dp[d[curr - target]]

    		dp[i] = max(dp[i-1], dp[i])

    		d[curr] = i

    	return dp[n]

