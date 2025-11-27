class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while (x or y):
            if x % 2 != y % 2:
                res += 1
            x = x >> 1
            y = y >> 1
            print(f"x: {x}, y:{y}")
        return res

if __name__ == "__main__":
    res = Solution().hammingDistance(x = 3, y = 1)
    print(res)