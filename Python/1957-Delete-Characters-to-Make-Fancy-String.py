class Solution:
    def makeFancyString(self, s: str) -> str:
        cnt = 1
        prev = s[0]
        res = s[0]
        for c in s[1:]:
            if c != prev:
                res += c
                prev = c
                cnt = 1
            elif cnt >= 2:
                cnt += 1
            else:
                res += c
                cnt += 1
        return res


if __name__ == "__main__":
    res = Solution().makeFancyString(s="leeetcode")
    print(res)

    res = Solution().makeFancyString(s="aaabaaaa")
    print(res)

    res = Solution().makeFancyString(s="aab")
    print(res)
