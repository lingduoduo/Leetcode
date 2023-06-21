import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def f(c):
            return ord(c) - 97

        ct_p, ct_s = [0] * 26, [0] * 26
        for c in s1:
            ct_p[f(c)] += 1

        l = len(s1)
        for c in s2[: l - 1]:
            ct_s[f(c)] += 1
        res = []
        for i, c in enumerate(s2[l - 1 :]):
            ct_s[f(c)] += 1
            if ct_s == ct_p:
                return True
            ct_s[f(s2[i])] -= 1
        return False


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        d1 = collections.Counter(s1)
        d2 = collections.Counter()

        m = len(s1)
        n = len(s2)

        left = 0
        right = 0
        while right < n:
            d2[s2[right]] += 1
            if right - left + 1 == m:
                if d2 == d1:
                    return True
                else:
                    d2[s2[left]] -= 1
                    if d2[s2[left]] == 0:
                        del d2[s2[left]]
                    left += 1
            right += 1
        return False
