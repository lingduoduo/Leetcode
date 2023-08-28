class Solution:
    def minimumSum(self, n: int, k: int) -> int:
        i = 0
        d = set()
        res = []
        w = 0
        while w < n:
            i += 1
            if k - i not in d:
                d.add(i)
                res.append(i)
                w += 1
        return sum(res)
