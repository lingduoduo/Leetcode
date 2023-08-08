import collections
import pysnooper


class Solution:
    @pysnooper.snoop()
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        cur = float("inf")

        start = 0
        debt = len(t)
        d = collections.Counter(t)
        for i, c in enumerate(s):
            d[c] -= 1
            if d[c] >= 0:
                debt -= 1
            while debt == 0:
                if cur > i - start + 1:
                    cur = i - start + 1
                    res = s[start : i + 1]
                d[s[start]] += 1
                if d[s[start]] > 0:
                    debt += 1
                start += 1
        return res


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    result = Solution().minWindow(S, T)
    print(result)
