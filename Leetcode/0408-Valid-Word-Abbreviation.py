class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        w1 = list(word)
        w2 = list(abbr)
        l = 0
        while w2:
            chr2 = w2.pop(0)
            if chr2 not in "0123456789":
                while l and w1:
                    w1.pop(0)
                    l -= 1
                if l > 0 or len(w1) == 0:
                    return False

                chr1 = w1.pop(0)
                if chr1 != chr2:
                    return False

            elif chr2 == "0" and l == 0:
                return False

            elif chr2 in list("0123456789"):
                l = l * 10 + int(chr2)

        while l and w1:
            w1.pop(0)
            l -= 1
        if l > 0:
            return False

        return l == 0 and len(w1) == 0

if __name__ == "__main__":
    res = Solution().validWordAbbreviation(word="internationalization", abbr="i12iz4n")
    print(res)

    res = Solution().validWordAbbreviation(word="apple", abbr="a2e")
    print(res)

    res = Solution().validWordAbbreviation(word="substitution", abbr="13")
    print(res)

    res = Solution().validWordAbbreviation(word="hi", abbr="2i")
    print(res)

