class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        ###"""
        ###nums = sorted(nums)
        ###return nums[len(nums) // 2]

        d = collections.Counter(nums)
        f = d.most_common()
        return f[0][0]
