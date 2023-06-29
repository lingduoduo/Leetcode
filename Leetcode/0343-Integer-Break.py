class Solution:
    def integerBreak(self, n: int) -> int:
        f = [1] * (1 + n)
        for i in range(2, n+ 1):
            for j in range(1, i // 2 + 1):
                f[i] = max(f[i], max(j, f[j]) * max(i - j, f[i - j]))
        return f[-1]
