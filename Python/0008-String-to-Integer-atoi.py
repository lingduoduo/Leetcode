class Solution:
    def myAtoi(self, str: str) -> int:
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()
        if str == "":
            return 0

        i = 0
        if str[i] == "-":
            flag = -1
            i += 1
        elif str[i] == "+":
            flag = 1
            i += 1
        else:
            flag = 1

        result = 0
        while i < len(str):
            if str[i] < "0" or str[i] > "9":
                break
            result = result * 10 + int(str[i])
            i += 1
        result = result * flag
        if result <= -(2**31):
            return -(2**31)
        if result >= 2**31:
            return 2**31 - 1
        return result

if __name__ == "__main__":
    print(Solution().myAtoi("+-12"))
    print(Solution().myAtoi("    -41"))
    print(Solution().myAtoi("4193 with words"))
    print(Solution().myAtoi("words and 987"))
    print(Solution().myAtoi("-91283472332"))
    print(Solution().myAtoi("3.14"))
