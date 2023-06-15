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
