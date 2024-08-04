class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return self.helper(s) == self.helper(t)

    def helper(self, word):
        res, d = [], {}
        for i, w in enumerate(word):
            if w not in d:
                d[w] = i
            res.append(d[w])
        return res


if __name__ == "__main__":
    s = "ab"
    t = "ca"
    result = Solution().isIsomorphic(s, t)
    print(result)
