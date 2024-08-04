import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = collections.Counter()
        start = 0
        res = 0
        for idx, cha in enumerate(s):
            d[cha] += 1
            maxCnt = d.most_common(1)[0][1]
            while idx - start + 1 - maxCnt > k:
                d[s[start]] -= 1
                start += 1
            res = max(res, idx - start + 1)
        return res


if __name__ == "__main__":
    s = "ABAB"
    res = Solution().characterReplacement(s, 1)
    print(res)
