class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i = 0
        word1 = list(word1)
        word2 = list(word2)
        res = []
        while word1 and word2:
            if i % 2 == 0:
                res.append(word1.pop(0))
            else:
                res.append(word2.pop(0))
            i += 1
        res = res + word1 + word2
        return "".join(res)
