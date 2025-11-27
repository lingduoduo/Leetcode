from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = -1
        idx2 = -1
        res = float("inf")
        for idx, word in enumerate(wordsDict):
            if word == word1:
                idx1 = idx
            if word == word2:
                idx2 = idx
            if idx1 != -1 and idx2 != -1:
                res = min(res, abs(idx1 - idx2))

        return res

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        idx1 = -1
        idx2 = -1
        res = float("inf")
        for idx, word in enumerate(wordsDict):
            if word == word1:
                if idx2 != -1:
                    res = min(res, idx - idx2)
                idx1 = idx
            if word == word2:
                if idx1 != -1:
                    res = min(res, idx - idx1)
                idx2 = idx
        return res


if __name__ == "__main__":
    words = ["practice", "makes", "perfect", "coding", "makes"]
    ###word1 = 'coding'
    ###word2 = 'practice'
    ###result = Solution().shortestDeistance(words, word1, word2)
    ###print(result)

    word1 = "makes"
    word2 = "coding"
    result = Solution().shortestDeistance(words, word1, word2)
    print(result)
