from typing import List
import collections


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n):
                self.p = list(range(n))

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

        uf, res, d = UF(len(s)), [], collections.defaultdict(list)
        for x, y in pairs:
            uf.union(x, y)

        for i in range(len(s)):
            d[uf.find(i)].append(s[i])

        for comp_id in d.keys():
            d[comp_id].sort(reverse=True)

        for i in range(len(s)):
            res.append(d[uf.find(i)].pop())

        return "".join(res)
