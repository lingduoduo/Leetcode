class Solution:
    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(x)-ord(y)) for x, y in zip(s, s[1:]))

if __name__ == "__main__":
    res = Solution().scoreOfString(s = "hello")
    print(res)