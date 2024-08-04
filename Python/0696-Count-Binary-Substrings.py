class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res = []
        for i in range(len(s) - 1):
            tmp = 1 if s[i] == "1" else -1
            j = i + 1
            while j < len(s) and s[j - 1] == s[j]:
                tmp += 1 if s[j] == "1" else -1
                j += 1
            if j == len(s) - 2:
                break
            j += 1
            tmp += 1 if s[j] == "1" else -1
            while j < len(s) and s[j - 1] == s[j]:
                tmp += 1 if s[j] == "1" else -1
                if tmp == 0:
                    res.append(s[i : j + 1])
                j += 1
        return res


class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        res, cur, pre = 0, 1, 0
        sLen = len(s)
        for i in range(1, sLen):
            if s[i] == s[i - 1]:  # count consecutive '0' or '1'
                cur += 1
            else:
                res += min(pre, cur)  # count qualified substrings
                pre = cur
                cur = 1
        res += min(pre, cur)  # count last series qualified substrings
        return res


if __name__ == "__main__":
    s = "00110011"
    res = Solution().countBinarySubstrings(s)
    print(res)
# ['0011', '00110011', '01', '0110', '011001', '1100', '10', '1001', '0011', '01']
# "0011", "01", "1100", "10", "0011", and "01"
