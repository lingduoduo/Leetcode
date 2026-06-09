class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        na, nb = len(a), len(b)
        times = nb // na + 1
        for i in range(1, times):
            if b in a * i:
                return i
        return -1


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        repeat = (len(b) + len(a) - 1) // len(a)
        text = a * (repeat + 1)


        def build_lps(pattern):
            lps = [0] * len(pattern)
            length = 0

            for i in range(1, len(pattern)):
                while length > 0 and pattern[i] != pattern[length]:
                    length = lps[length - 1]

                if pattern[i] == pattern[length]:
                    length += 1
                    lps[i] = length

            return lps

        lps = build_lps(b)
        j = 0

        for i in range(len(text)):
            while j > 0 and text[i] != b[j]:
                j = lps[j - 1]

            if text[i] == b[j]:
                j += 1

            if j == len(b):
                end = i + 1
                return (end + len(a) - 1) // len(a)

        return -1

