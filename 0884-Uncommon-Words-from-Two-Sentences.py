class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        words = (A + " " + B).split(" ")
        d = collections.Counter(words)
        res = [k for k, v in d.items() if v == 1]
        return res
        