import collections
from typing import List


class Solution:
    def checkSubarraySum(self, nums, k) -> bool:
        dp = collections.defaultdict()
        dp[0] = -1
        tot = 0
        m = -1
        for i, num in enumerate(nums):
            print(dp)
            tot += num
            if k == 0:
                m = tot
            else:
                m = tot % k
            if dp.get(m) == None:
                dp[m] = i
            elif i - dp[m] > 1:
                return True
        return False


class Solution:
    def checkSubarraySum(self, nums, k: int) -> bool:
        d = collections.defaultdict(int)
        tot = 0
        for idx, num in enumerate(nums):
            tot += num
            m = tot if k == 0 else tot % k
            if m in d and idx - d[m] >= 1:
                return True
            d[m] = idx
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hash_map = {0: 0}
        s = 0
        for i in range(len(nums)):
            s += nums[i]
            if s % k not in hash_map:
                hash_map[s % k] = i + 1
            elif hash_map[s % k] < i:
                return True
        return False


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        presum = 0
        d = collections.Counter()
        d[0] = 0
        for i, num in enumerate(nums):
            presum += num
            if presum % k not in d:
                d[presum % k] = i + 1
            elif d[presum % k] < i:
                return True
        return False


if __name__ == "__main__":
    nums = [23, 2, 4, 6, 7]
    k = 6
    results = Solution().checkSubarraySum(nums, k)
    print(results)

    nums = [23, 2, 6, 4, 7]
    k = 0
    results = Solution().checkSubarraySum(nums, k)
    print(results)

    nums = [0]
    k = 0
    results = Solution().checkSubarraySum(nums, k)
    print(results)

    nums = [0, 1, 0]
    k = 0
    results = Solution().checkSubarraySum(nums, k)
    print(results)

    nums = [2, 2]
    k = 2
    results = Solution().checkSubarraySum(nums, k)
    print(results)
