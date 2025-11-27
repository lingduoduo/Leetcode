from typing import List


class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        d = set(words)
        for word in words:
            d.remove(word)
            n = len(word)
            if n == 0:
                continue
            dp = [False] * (1 + n)
            dp[0] = True
            for i in range(1 + n):
                for j in range(i):
                    if dp[j] and word[j:i] in d:
                        dp[i] = True
                        break
            if dp[-1]:
                res.append(word)
            d.add(word)
        return res
