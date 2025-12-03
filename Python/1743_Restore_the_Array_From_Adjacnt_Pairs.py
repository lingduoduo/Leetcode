from collections import defaultdict
from typing import List

class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for x, y in adjacentPairs:
            d[x].append(y)
            d[y].append(x)

        # find a start: an endpoint, which has only one neighbor
        start = None
        for k, v in d.items():
            if len(v) == 1:
                start = k
                break

        n = len(adjacentPairs) + 1
        res = [0] * n
        res[0] = start
        res[1] = d[start][0]

        for i in range(2, n):
            prev = res[i - 2]
            cur = res[i - 1]
            # neighbors of cur are in d[cur]; pick one that's not prev
            nbrs = d[cur]
            if nbrs[0] == prev:
                res[i] = nbrs[1]
            else:
                res[i] = nbrs[0]

        return res
