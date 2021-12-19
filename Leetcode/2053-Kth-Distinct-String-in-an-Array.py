import collections
from collections import Counter
from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = collections.Counter(arr)
        print(d)
        for kd, vd in d.items():
            if vd == 1:
                if k == 1:
                    return kd
                k -= 1
        if k >= 1:
            return ""


if __name__ == "__main__":
    res = Solution().kthDistinct(arr=["d", "b", "c", "b", "c", "a"], k=2)
    print(res)
    res = Solution().kthDistinct(arr = ["aaa","aa","a"], k = 1)
    print(res)
    res = Solution().kthDistinct(arr = ["a","b","a"], k = 3)
    print(res)

