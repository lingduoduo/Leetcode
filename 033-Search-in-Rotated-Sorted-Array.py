class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if nums is None:
        	return -1

        for i in len(range(nums)):
        	if target == nums[i]:
        		return i

        return -1
