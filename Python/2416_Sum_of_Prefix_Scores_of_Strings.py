from typing import List


class Trie:
    def __init__(self):
        self.d = {}
        self.count = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = Trie()

        # Build Trie
        for word in words:
            node = root

            for ch in word:
                if ch not in node.d:
                    node.d[ch] = Trie()

                node = node.d[ch]
                node.count += 1

        # Query scores
        ans = []

        for word in words:
            node = root
            score = 0

            for ch in word:
                node = node.d[ch]
                score += node.count

            ans.append(score)

        return ans