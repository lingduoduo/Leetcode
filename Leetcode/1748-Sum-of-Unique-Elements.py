from typing import List
import collections


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        d = collections.Counter(nums)

        res = 0
        for k, v in d.items():
            if v == 1:
                res += k
        return res


if __name__ == "__main__":
    nums = [1, 2, 3, 2]
    res = Solution().sumOfUnique(nums)
    print(res)
