from typing import List
import collections


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        d = collections.Counter(nums)
        t = sum([v // 2 for v in d.values()])
        l = sum([1 for v in d.values() if v % 2 == 1])
        return [t, l]


if __name__ == "__main__":
    res = Solution().numberOfPairs(nums=[1, 3, 2, 1, 3, 2, 2])
    print(res)

    res = Solution().numberOfPairs(nums=[0])
    print(res)
