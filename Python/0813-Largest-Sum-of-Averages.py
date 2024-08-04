class Solution:
    def largestSumOfAverages(self, A: List[int], K: int) -> float:
        n = len(A)
        m = [[0] * (1 + n) for _ in range(1 + K)]
        tot = [0] * (1 + n)

        for i in range(1, 1 + n):
            tot[i] = tot[i - 1] + A[i - 1]

        return self.LSA(A, tot, m, n, K)

    def LSA(self, A, tot, m, n, k):
        if m[k][n] > 0:
            return m[k][n]
        if k == 1:
            return tot[n] / n
        for i in range(k - 1, n):
            m[k][n] = max(
                m[k][n], self.LSA(A, tot, m, i, k - 1) + (tot[n] - tot[i]) / (n - i)
            )
        return m[k][n]
