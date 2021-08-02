import re
class Solution:
    def isNumeric(self, s):
        if len(s) == 0:
            return None

        return re.search(r"[+-]?\d*(\.\d+)?([eE][+-]?\d+)?", s).group() == s


if __name__ == '__main__':

    res = Solution().isNumeric(s="+100")
    print(res)

    res = Solution().isNumeric(s="5e2")
    print(res)

    res = Solution().isNumeric(s="-123")
    print(res)

    res = Solution().isNumeric(s="+100")
    print(res)

    res = Solution().isNumeric(s="3.1416")
    print(res)

    res = Solution().isNumeric(s="-1E-16")
    print(res)


    res = Solution().isNumeric(s="12e")
    print(res)

    res = Solution().isNumeric(s="1.2.3")
    print(res)

    res = Solution().isNumeric(s="12e+4.3")
    print(res)

