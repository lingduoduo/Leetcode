class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        d = collections.Counter(nums)
        for k, v in d.items():
            if v == 1:
                return k
