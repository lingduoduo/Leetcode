import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = collections.Counter(t)
        l = 0
        r = 0                 
        size = float("inf")
        res = ""

        for i, ch in enumerate(s):
            if ch in d:
                d[ch] -= 1
                if d[ch] >= 0:
                    r += 1

            while r == len(t):
                if i - l + 1 < size:
                    size = i - l + 1
                    res = s[l:i + 1]

                if s[l] in d:
                    d[s[l]] += 1
                    if d[s[l]] > 0:
                        r -= 1
                l += 1

        return res


if __name__ == "__main__":
    S = "ADOBECODEBANC"
    T = "ABC"
    result = Solution().minWindow(S, T)
    print(result)
