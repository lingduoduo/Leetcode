class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        res = 0
        for word in words:
            w = set(word)
            if w.issubset(allowed):
                res += 1
        return res
