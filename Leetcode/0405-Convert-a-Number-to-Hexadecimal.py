class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        d = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
        if num < 0:
            num += 1 << 32
        for i in range(10):
            d[i] = str(i)

        res = ""
        while num != 0:
            res = d[num % 16] + res
            num = num // 16
        return res


if __name__ == "__main__":
    results = Solution().toHex(-1)
    print(results)
