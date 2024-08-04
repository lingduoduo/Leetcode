class Solution:
    def maxSumTwoNoOverlap(self, A: List[int], L: int, M: int) -> int:
        sums = [0] * len(A)
        sums[0] = A[0]
        for i in range(1, len(A)):
            sums[i] = sums[i - 1] + A[i]

        res = 0
        for i in range(len(A) - L + 1):
            for j in range(len(A) - M + 1):
                if i == 0 and j == 2:
                    pass
                if (j + M - 1) < i or (i + L - 1) < j:
                    v2 = sums[j + M - 1]
                    if j >= 1:
                        v2 -= sums[j - 1]
                    v1 = sums[i + L - 1]
                    if i >= 1:
                        v1 -= sums[i - 1]
                    res = max(res, v1 + v2)
        return res


if __name__ == "__main__":
    A = [0, 6, 5, 2, 2, 5, 1, 9, 4]
    L = 1
    M = 2
    Solution().maxSumTwoNoOverlap(A, L, M)
