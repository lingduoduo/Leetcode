from typing import List

class Solution:
    def singleNumber(self, nums) -> int:
        res = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                cnt += (num >> i) & 1
            res |= (cnt % 3) << i
        return res - 2 ** 32 if res >> 31 & 1 else res

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen_once = seen_twice = 0
        for num in nums:
            seen_once = ~seen_twice & (seen_once ^ num)
            seen_twice = ~seen_once & (seen_twice ^ num)
        return seen_once


import collections
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d = collections.Counter(nums)
        for k, v in d.items():
            if v == 1:
                return k


if __name__ == '__main__':
    nums = [2, 2, 3, 2]
    results = Solution().singleNumber(nums)
    print(results)
