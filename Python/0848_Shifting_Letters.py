class Solution:
    def shiftingLetters(self, S, shifts):
        r = shifts[::-1]
        s = [0] * (1 + len(r))
        for i in range(len(r)):
            s[i + 1] = s[i] + r[i]
        s = s[1:]
        s = s[::-1]
        res = ""
        for i in range(len(s)):
            res += chr((ord(S[i]) - ord("a") + s[i]) % 26 + ord("a"))
        return res


if __name__ == "__main__":
    shifts = [3, 5, 9]
    result = Solution().shiftingLetters("abc", shifts)
    print(result)
    shifts = [26, 9, 17]
    result = Solution().shiftingLetters("ruu", shifts)
    print(result)
