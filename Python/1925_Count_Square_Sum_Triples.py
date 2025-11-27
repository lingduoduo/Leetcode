import math


class Solution:
    def countTriples(self, n: int) -> int:
        res = 0
        for a in range(1, 1 + n):
            for b in range(1, 1 + n):
                c = int(math.sqrt(a**2 + b**2 + 1))
                if c <= n and c**2 == a**2 + b**2:
                    res += 1
        return res


if __name__ == "__main__":
    res = Solution().countTriples(10)
    print(res)
