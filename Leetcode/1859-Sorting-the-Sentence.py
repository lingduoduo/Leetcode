class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split(" ")
        res = [""] * 9
        cnt = 0
        for word in words:
            pos = int(word[-1])
            res[pos-1] += word[:-1]
        return ' '.join(res[:len(words)])

if __name__ == "__main__":
    res = Solution().sortSentence(s = "is2 sentence4 This1 a3")
    print(res)

    res = Solution().sortSentence(s = "Myself2 Me1 I4 and3")
    print(res)