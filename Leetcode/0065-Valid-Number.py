class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()  # 去除首尾空格

        isDot, isDigit, isE = False, False, False  # 点，数字，e

        for i, x in enumerate(s):
            if x == "e":
                if not isDigit or isE:  # 前面没有数字，or 前面已经存在字符 e
                    return False

                isDigit = False  # 设置isDigit = false
                isE = True
            elif x in "+-":
                if i != 0 and s[i - 1] != "e":  # +- 只能出现首位，和 字符e的后面
                    return False
            elif x == ".":
                if isDot or isE:  # 字符 .（小数点）只能出现一次，而且是只能出现在 e 的前面
                    return False
                isDot = True
            elif x.isdecimal():  # 检查字符串是否只包含十进制字符
                isDigit = True
            else:
                return False

        return len(s) > 0 and isDigit


import re

class Solution:
    def isNumber(self, s: str) -> bool:
        pattern = re.compile(r'^[+-]?(\d+|\d+\.\d*|\.\d+)([eE][+-]?\d+)?$')
        return pattern.match(s) is not None


class Solution:
    def isNumber(self, s: str) -> bool:
        seen_digit = seen_exponent = seen_dot = False
        for i, c in enumerate(s):
            if c.isdigit():
                seen_digit = True
            elif c in ["+", "-"]:
                if i > 0 and s[i - 1] != "e" and s[i - 1] != "E":
                    return False
            elif c in ["e", "E"]:
                if seen_exponent or not seen_digit:
                    return False
                seen_exponent = True
                seen_digit = False
            elif c == ".":
                if seen_dot or seen_exponent:
                    return False
                seen_dot = True
            else:
                return False

        return seen_digit

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
