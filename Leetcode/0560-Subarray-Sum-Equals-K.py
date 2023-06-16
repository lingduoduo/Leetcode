from typing import List


class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        d = collections.defaultdict(int)
        d[0] = 1
        presum = 0
        res = 0
        for i in range(len(nums)):
            presum += nums[i]
            if presum - k in d:
                res += d[presum - k]
            d[presum] += 1
        return res


if __name__ == "__main__":
    res = Solution().subarraySum(nums=[1, 1, 1], k=2)
    print(res)
