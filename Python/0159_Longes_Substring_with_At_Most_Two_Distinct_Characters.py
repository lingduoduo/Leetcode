import collections


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        n = len(s)
        if n < 3:
            return n
        left, right = 0, 0
        d = collections.defaultdict(int)
        res = 0
        for cha in s:
            d[cha] += 1
            if len(d.keys()) > 2:
                while len(d.keys()) > 2:
                    d[s[left]] -= 1
                    if d[s[left]] == 0:
                        d.pop(s[left])
                    left += 1
            right += 1
            res = max(res, right - left)
        return res


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        start = 0
        d = collections.Counter()
        res = 0
        for i, v in enumerate(s):
            d[v] += 1
            if len(d.keys()) <= 2:
                res = max(res, i - start + 1)
            while len(d.keys()) > 2:
                d[s[start]] -= 1
                if d[s[start]] == 0:
                    del d[s[start]]
                start += 1
        return res


if __name__ == "__main__":
    res = Solution().lengthOfLongestSubstringTwoDistinct(s="ccaabbb")
    print(res)
