class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d = Counter(s)

        for i, cha in enumerate(t):
            if cha not in d:
                return cha
            elif d[cha] == 0:
                return cha
            else:
                d[cha] -= 1
