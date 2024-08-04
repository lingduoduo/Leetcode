class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split(" ")
        res = 0
        for word in words:
            wordset = list(set(word)) + list(brokenLetters)
            if len(wordset) == len(set(wordset)):
                res += 1
        return res


if __name__ == "__main__":
    res = Solution().canBeTypedWords(text="leet code", brokenLetters="e")
    print(res)

    res = Solution().canBeTypedWords(text="word test", brokenLetters="e")
    print(res)
