import collections


class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        for x, y in edges:
            d[x].append(y)
            d[y].append(x)

        n = len(d.keys())
        for k in d:
            if len(d[k]) == n - 1:
                return k
