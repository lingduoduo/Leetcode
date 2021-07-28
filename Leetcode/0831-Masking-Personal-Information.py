class Solution:
    def maskPII(self, s: str) -> str:
        res = []
        if "@" in s:
            names = s.split("@")
            res.append(names[0][0])
            res.append("*****")
            res.append(names[0][-1])
            res.append("@")
            res.extend(names[1:])
            return ''.join(res).lower()
        else:
            for cha in s:
                if cha in "0123456789":
                    res.append(cha)

            if len(res) == 10:
                return "***-***-" + ''.join(res[-4:])
            else:
                return "+" + '*' * (len(res) - 10) + "-***-***-" + ''.join(res[-4:])

if __name__ == '__main__':
    res = Solution().maskPII(s="LeetCode@LeetCode.com")
    print(res)

    res = Solution().maskPII(s="1(234)567-890")
    print(res)

    res = Solution().maskPII(s="86-(10)12345678")
    print(res)