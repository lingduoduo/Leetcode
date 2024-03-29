class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x

        def lcm2(x, y):
            return x * y // gcd(x, y)

        def lcm3(x, y, z):
            res = x * y // gcd(x, y)
            return res * z // gcd(z, res)

        def cnt(k, x, y, z):
            return (
                k // x
                + k // y
                + k // z
                - k // lcm2(x, y)
                - k // lcm2(x, z)
                - k // lcm2(y, z)
                + k // lcm3(x, y, z)
            )

        l, r = 1, 2 * 10**9
        while l < r:
            mid = (l + r) >> 1
            if cnt(mid, a, b, c) < n:
                l = mid + 1
            else:
                r = mid
        return l


if __name__ == "__main__":
    # n = 3
    # a = 2
    # b = 3
    # c = 5
    # n = 5
    # a = 2
    # b = 11
    # c = 13
    n = 1000000000
    a = 2
    b = 217983653
    c = 336916467
    results = Solution().nthUglyNumber(n, a, b, c)
    print(results)
