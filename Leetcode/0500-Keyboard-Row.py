import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rowdict = {}
        for c in "qwertyuiopQWERTYUIOP":
            rowdict[c] = 1
        for c in "asdfghjklASDFGHJKL":
            rowdict[c] = 2
        for c in "zxcvbnmZXCVBNM":
            rowdict[c] = 3

        res = []
        for word in words:
            curr = []
            for i in range(len(word)):
                curr.add(rowdict[word[i]])
            if len(set(curr)) == 1:
                res.append(word)
        return res
