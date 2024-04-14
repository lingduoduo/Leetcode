import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res = ""
        cur = float("inf")

        start = 0
        t_len = len(t)
        t_d = collections.Counter(t)
        for i, c in enumerate(s):
            t_d[c] -= 1
            if t_d[c] >= 0:
                t_len -= 1
            while t_len == 0:
                if cur > i - start + 1:
                    cur = i - start + 1
                    res = s[start : i + 1]
                t_d[s[start]] += 1
                if t_d[s[start]] > 0:
                    t_len += 1
                start += 1
        return res


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    result = Solution().minWindow(S, T)
    print(result)
