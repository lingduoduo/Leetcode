from typing import List

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        d = collections.defaultdict(int)
        d[0] = 1
        tot = 0
        res = 0
        for i in range(n):
            tot += nums[i]
            if tot - k in d:
                res += d[tot - k]
            d[tot] += 1
        return res

if __name__ == "__main__":
    res = Solution().subarraySum(nums=[1, 1, 1], k=2)
    print(res)
