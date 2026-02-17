from typing import List
from collections import defaultdict

class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            d = defaultdict(int)
            for j in range(i, n):
                d[s[j]] += 1
                if len(set(d.values())) == 1:
                    res = max(res, j - i + 1)
        return res


if __name__ == "__main__":
    res = Solution().longestBalanced(s = "zzabccy")
    print(res)