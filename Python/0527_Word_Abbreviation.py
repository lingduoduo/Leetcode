from typing import List
from collections import defaultdict

class Solution:
    def wordsAbbreviation(self, words: List[str]) -> List[str]:
        def abbr(word: str, k: int) -> str:
            # 保留前 k 个字符
            if len(word) - k <= 2:
                return word
            return word[:k] + str(len(word) - k - 1) + word[-1]

        n = len(words)
        prefix = [1] * n
        res = [abbr(word, 1) for word in words]

        while True:
            groups = defaultdict(list)
            for i, a in enumerate(res):
                groups[a].append(i)

            unique = True
            for idxs in groups.values():
                if len(idxs) > 1:
                    unique = False
                    for i in idxs:
                        prefix[i] += 1
                        res[i] = abbr(words[i], prefix[i])

            if unique:
                break

        return res