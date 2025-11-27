###Given a list of words and two words word1 and word2, return the shortest
###distance between these two words in the list.

###For example,
###Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

###Given word1 = “coding”, word2 = “practice”, return 3.
###Given word1 = "makes", word2 = "coding", return 1.

###Note:
###You may assume that word1does not equal toword2, and word1 and word2 are
###both in the list.

###这道题小心重复


import collections
from typing import List
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.dict = collections.defaultdict(list)
        for i, w in enumerate(wordsDict):
            self.dict[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        w1 = self.dict[word1]
        w2 = self.dict[word2]
        res = min(abs(word1-word2)for word1 in w1 for word2 in w2)
        return res

wordsDict = ["practice", "makes", "perfect", "coding", "makes"]
obj = WordDistance(wordsDict)
print(obj.shortest("makes", "coding"))

