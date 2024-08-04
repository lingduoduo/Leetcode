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
        pattern = re.compile(r"^[+-]?(\d+|\d+\.\d*|\.\d+)([eE][+-]?\d+)?$")
        return pattern.match(s) is not None


"""
Algorithm

1. Declare 3 variables seenDigit, seenExponent, and seenDot. Set all of them to false.
2. Iterate over the input.
3. If the character is a digit, set seenDigit = true.
4. If the character is a sign, check if it is either the first character of the input, or if the character before it is an exponent. If not, return false.
5. If the character is an exponent, first check if we have already seen an exponent or if we have not yet seen a digit. If either is true, then return false. Otherwise, set seenExponent = true, and seenDigit = false. We need to reset seenDigit because after an exponent, we must construct a new integer.
6. If the character is a dot, first check if we have already seen either a dot or an exponent. If so, return false. Otherwise, set seenDot = true.
7. If the character is anything else, return false.
8. At the end, return seenDigit. This is one reason why we have to reset seenDigit after seeing an exponent - otherwise an input like "21e" would be incorrectly judged as valid.
"""


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


if __name__ == "__main__":
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
