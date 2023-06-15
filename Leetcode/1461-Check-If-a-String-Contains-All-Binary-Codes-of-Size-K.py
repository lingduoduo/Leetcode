class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        d = set()
        for i in range(len(s) - k + 1):
            d.add(s[i : (i + k)])
        return len(d) == 2**k


if __name__ == "__main__":
    # s = "00110110"
    s = "00110"
    k = 2
    res = Solution().hasAllCodes(s, k)
    print(res)
