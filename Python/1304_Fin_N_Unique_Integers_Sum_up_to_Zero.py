class Solution:
    def sumZero(self, n: int):
        res = []
        if n % 2 == 1:
            res.append(0)
        for i in range(1, n // 2 + 1):
            res.append(i)
            res.append(-i)
        return res


if __name__ == "__main__":
    result = Solution().sumZero(2)
    print(result)
