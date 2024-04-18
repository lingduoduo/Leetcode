class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        prev = dict()
        curr = dict()
        for i in range(len(A)):
            d = collections.Counter(A[i])
            if i == 0:
                prev = d
                curr = d
            else:
                prev = curr
                keys = curr.keys() & d.keys()
                curr = dict()
                for key in keys:
                    curr[key] = min(prev[key], d[key])
        res = []
        for k, v in curr.items():
            res.extend([k] * v)
        return res

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        freq = collections.Counter(words[0])
        for word in words[1:]:
            freq &= collections.Counter(word)
        res = []
        for k, v in freq.items():
            res.extend([k] * v)
        return res