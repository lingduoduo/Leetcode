class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        d = collections.Counter()
        start = 0
        res = 0
        for i, v in enumerate(s):
            d[v] += 1
            while len(d.keys()) > k:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1
            res = max(res, i - start + 1)
        return res
