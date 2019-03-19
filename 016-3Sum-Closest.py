class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        result = float('inf')
        nums = sorted(nums)

        for i in range(len(nums)):
        	j = i+1
        	k = len(nums)-1
        	while j<k:
        		if nums[i] + nums[j] + nums[k] == target:
        			return target

        		if abs((nums[i] + nums[j] + nums[k])-target) < abs(result-target):
        			result = nums[i] + nums[j] + nums[k]

        		if nums[i] + nums[j] + nums[k] < target:
        			j+=1

        		if nums[i] + nums[j] + nums[k] > target:
        			k-=1
        return result

if __name__=="__main__":
    nums=[-1, 2, 1, -4]
    # nums = [-1,-5,-3,-4,2,-2]
    result = Solution().threeSumClosest(nums, 1)
    print(result)