class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        cur = -1
        d = {}
        word += "#"
        for i, w in enumerate(word):
            if w in "0123456789":
                if cur == -1:
                    cur = int(w)
                else:
                    cur = cur * 10 + int(w)
            else:
                if cur >= 0:
                    d[cur] = d.get(cur, 0) + 1
                cur = -1
        return len(d.keys())


if __name__ == "__main__":
    word = "a123bc34d8ef34"
    res = Solution().numDifferentIntegers(word)
    print(res)

    word = "0a0"
    res = Solution().numDifferentIntegers(word)
    print(res)
