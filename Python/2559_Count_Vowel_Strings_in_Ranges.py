from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        presum = [0]
        for word in words:
            if word[0] in "aeiou" and word[-1] in "aeiou":
                presum.append(presum[-1] + 1)
            else:
                presum.append(presum[-1])

        res = []
        for s, e in queries:
            res.append(presum[e + 1] - presum[s])
        return res


if __name__ == "__main__":
    res = Solution().vowelStrings(words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]])
    print(res)