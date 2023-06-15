class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        wmap = {w: i for i, w in enumerate(words)}

        res = set()
        for idx, word in enumerate(words):
            if word and word == word[::-1] and "" in wmap:
                nidx = wmap[""]
                res.add((idx, nidx))
                res.add((nidx, idx))

            rword = word[::-1]
            if word and rword in wmap:
                nidx = wmap[rword]
                if idx != nidx:
                    res.add((idx, nidx))
                    res.add((nidx, idx))

            for x in range(1, len(word)):
                left, right = word[:x], word[x:]
                rleft, rright = left[::-1], right[::-1]
                if left == left[::-1] and right[::-1] in wmap:
                    res.add((wmap[rright], idx))
                if right == right[::-1] and left[::-1] in wmap:
                    res.add((idx, wmap[rleft]))
        return list(res)
