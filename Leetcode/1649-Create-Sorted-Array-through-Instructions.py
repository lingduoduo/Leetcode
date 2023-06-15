class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        def update(k):
            while k <= limit:
                range_sum[k] += 1
                k += k & -k

        def query(k):
            res = 0
            while k:
                res += range_sum[k]
                k -= k & -k
            return res

        limit = max(instructions)
        range_sum = [0] * (limit + 1)
        res = 0
        MOD = 10**9 + 7
        for i, n in enumerate(instructions):
            res += min(query(n - 1), i - query(n)) % MOD
            update(n)
        return res % MOD
