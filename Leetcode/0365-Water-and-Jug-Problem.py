class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        return z == 0 or (x + y >= z and z % self.gcd(x, y) == 0)

    def gcd(self, x, y):
        print([x, y])
        return x if y == 0 else self.gcd(y, x % y)


if __name__ == "__main__":
    g = Solution().gcd(3, 5)
    print(g)
