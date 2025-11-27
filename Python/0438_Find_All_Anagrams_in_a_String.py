from typing import List
import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        n = len(s)
        l = len(p)
        vp = [0] * 26
        vs = [0] * 26
        results = list()
        for cha in p:
            vp[ord(cha) - ord("a")] += 1
        for i in range(n):
            if i >= l:
                vs[ord(s[i - l]) - ord("a")] -= 1
            vs[ord(s[i]) - ord("a")] += 1
            if vp == vs:
                results.append(i + 1 - l)
        return results


class Solution(object):
    def findAnagrams(self, s, p):
        def f(c):
            return ord(c) - 97

        ct_p, ct_s = [0] * 26, [0] * 26
        for c in p:
            ct_p[f(c)] += 1

        l = len(p)
        for c in s[: l - 1]:
            ct_s[f(c)] += 1

        res = []
        for i, c in enumerate(s[l - 1 :]):
            ct_s[f(c)] += 1
            if ct_s == ct_p:
                res.append(i)
            ct_s[f(s[i])] -= 1
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        d = collections.Counter(p)
        res = []
        for i in range(len(s) - len(p) + 1):
            if s[i] not in d:
                continue
            if collections.Counter(s[i : i + len(p)]) == d:
                res.append(i)
        return res


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        s_dict = collections.Counter()
        p_dict = collections.Counter(p)
        m, n = len(s), len(p)
        left, right = 0, 0
        res = []
        while right < m:
            s_dict[s[right]] += 1
            if right - left + 1 == n:
                if s_dict == p_dict:
                    res.append(left)
                s_dict[s[left]] -= 1
                if s_dict[s[left]] == 0:
                    del s_dict[s[left]]
                left += 1
            right += 1
        return res


if __name__ == "__main__":
    s = "abab"
    p = "ab"
    print(Solution().findAnagrams(s, p))
