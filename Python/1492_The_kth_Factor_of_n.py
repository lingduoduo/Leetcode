class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        res = set()
        for i in range(1, 1 + int(math.sqrt(n))):
            if n % i == 0:
                res.add(i)
                res.add(n // i)
        res = list(res)
        if len(res) < k:
            return -1
        else:
            res.sort()
            return res[k - 1]
