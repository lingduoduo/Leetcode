import collections


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        d = []
        for i, n in enumerate(s1):
            if s1[i] != s2[i]:
                d.append(i)
        if len(d) != 2:
            return False
        return s1[d[0]] == s2[d[1]] and s1[d[1]] == s2[d[0]]


if __name__ == "__main__":
    s1 = "caa"
    s2 = "aaz"
    res = Solution().areAlmostEqual(s1, s2)
    print(res)
