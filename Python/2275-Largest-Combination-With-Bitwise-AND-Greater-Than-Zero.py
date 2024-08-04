from typing import List
from functools import reduce


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        return max(sum(n & (1 << i) > 0 for n in candidates) for i in range(0, 24))



if __name__ == "__main__":
    res = Solution().largestCombination(candidates = [8, 8])
    print(res)

