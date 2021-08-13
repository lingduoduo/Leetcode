class Solution:
    def add(self, a, b) -> int:
        return a if b == 0 else self.add(a ^ b, (a & b) << 1)


if __name__ == '__main__':
    res = Solution().add(a = 2, b = 4)
    print(res)

