from collections import defaultdict


class Solution:
    def gridIllumination(
        self, N: int, lamps: List[List[int]], queries: List[List[int]]
    ) -> List[int]:
        ctx = defaultdict(int)
        cty = defaultdict(int)
        ctd = defaultdict(int)
        ctad = defaultdict(int)
        res = []
        s = set([tuple(x) for x in lamps])
        for x, y in lamps:
            ctx[x] += 1
            cty[y] += 1
            ctd[x + y] += 1
            ctad[x - y] += 1
        directions = [
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (0, -1),
            (0, 0),
            (0, 1),
            (1, -1),
            (1, 0),
            (1, 1),
        ]
        for x, y in queries:
            if ctx[x] > 0 or cty[y] or ctd[x + y] > 0 or ctad[x - y] > 0:
                res.append(1)
            else:
                res.append(0)
            for dirx, diry in directions:
                p, q = x + dirx, y + diry
                if (p, q) in s:
                    s.remove((p, q))
                    ctx[p] -= 1
                    cty[q] -= 1
                    ctd[p + q] -= 1
                    ctad[p - q] -= 1
        return res
