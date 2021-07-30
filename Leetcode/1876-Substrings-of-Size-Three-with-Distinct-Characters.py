class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)-2):
            if len(s[i:i+3]) == len(set(s[i:i+3])):
                res += 1
        return res

if __name__ == '__main__':
    res = Solution().countGoodSubstrings(s="xyzzaz")
    print(res)
