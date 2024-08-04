from collections import Counter


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) > len(str2):
            str1, str2 = str2, str1

        cnt1 = Counter(str1)
        cnt2 = Counter(str2)
        if [k for k in cnt1] != [k for k in cnt2]:
            return ""

        i = len(str1)
        while i > 0:
            m1 = len(str2) // len(str1[:i])
            m2 = len(str1) // len(str1[:i])
            if str2 == str1[:i] * m1 and str1 == str1[:i] * m2:
                return str1[:i]
            else:
                i -= 1
        return ""
