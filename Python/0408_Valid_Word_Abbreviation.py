class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0
        while i < len(word) and j < len(abbr):
            if word[i] == abbr[j]:
                i += 1
                j += 1
            else:
                if abbr[j] == "0" or abbr[j].isalpha():
                    return False
                num = 0
                while j < len(abbr) and abbr[j].isdigit():
                    num = num * 10 + int(abbr[j])
                    j += 1
                i += num
        return i == len(word) and j == len(abbr)


if __name__ == "__main__":
    res = Solution().validWordAbbreviation(word="internationalization", abbr="i12iz4n")
    print(res)

    res = Solution().validWordAbbreviation(word="apple", abbr="a2e")
    print(res)

    res = Solution().validWordAbbreviation(word="substitution", abbr="13")
    print(res)

    res = Solution().validWordAbbreviation(word="hi", abbr="2i")
    print(res)
