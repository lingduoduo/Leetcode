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
                if i != 0 and s[i-1] != "e":  # +- 只能出现首位，和 字符e的后面
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
