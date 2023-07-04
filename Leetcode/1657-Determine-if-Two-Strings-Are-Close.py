import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        return set(word1) == set(word2) and collections.Counter(
            collections.Counter(word1).values()
        ) == collections.Counter(collections.Counter(word2).values())
