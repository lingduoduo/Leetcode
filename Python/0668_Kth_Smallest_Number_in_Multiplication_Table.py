class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m

        l, r = 0, m * n
        while l < r:
            mid = l + (r - l) // 2

            count = 0
            for i in range(1, m + 1):
                count += min(n, mid // i)

            if count < k:
                l = mid + 1
            else:
                r = mid

        return l
