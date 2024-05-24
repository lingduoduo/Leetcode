class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        res = float('inf')
        prevIndex = -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1 or wordsDict[i] == word2:
                if prevIndex != -1 and (wordsDict[prevIndex] != wordsDict[i] or word1 == word2):
                    res = min(res, i - prevIndex)
                prevIndex = i

        return res