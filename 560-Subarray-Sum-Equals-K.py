class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        prefix = [0]*(1+len(nums))
        
        for i in range(1,len(nums)+1):
        	prefix[i] = prefix[i-1] + nums[i]

        res = 0
        for i in range(0, len(nums)+1):
        	for j in range(i+1, len(nums)+1):
        		if prefix[j] - prefix[i] == k:
        			res+=1
        return res

