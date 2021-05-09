class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A = sorted(set(A))
        lo, hi = A[0], A[-1]
        res = hi - lo
        if res <= K:
            return res
        if res >= 4 * K:
            return res - K * 2
        for i in range(len(A) - 1):
            a, b = A[i], A[i + 1]
            res = min(res, max(hi - K, a + K) - min(lo + K, b - K))
        return res

