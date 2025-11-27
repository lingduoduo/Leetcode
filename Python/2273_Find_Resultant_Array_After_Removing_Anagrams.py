from collections import Counter
from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]
        for i in range(1,len(words)):
            if Counter(res[-1]) != Counter(words[i]):
                res.append(words[i])
        return res


if __name__ == "__main__":
    res = Solution().removeAnagrams(["abba","baba","bbaa","cd","cd"])
    print(res)
    res = Solution().removeAnagrams(["a","b","c","d","e"])
    print(res)



