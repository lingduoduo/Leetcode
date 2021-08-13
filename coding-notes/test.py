class Solution:
    def strToInt(self, strs):
        if not strs:
            return 0 
        flag = strs[0] == "-"
        res = 0
        for char in strs:
            if char == "+" or char == "-":
                continue
            if char < "0" or char > "9":
                return 0
            res = res * 10 + ord(char) - ord("0")
        return -res if flag else res


if __name__ == '__main__':
    res = Solution().strToInt(strs = "+2147483647")
    print(res)



# public int StrToInt(String str) {
#     if (str == null || str.length() == 0)
#         return 0;
#     boolean isNegative = str.charAt(0) == '-';
#     int ret = 0;
#     for (int i = 0; i < str.length(); i++) {
#         char c = str.charAt(i);
#         if (i == 0 && (c == '+' || c == '-'))  /* 符号判定 */
#             continue;
#         if (c < '0' || c > '9')                /* 非法输入 */
#             return 0;
#         ret = ret * 10 + (c - '0');
#     }
#     return isNegative ? -ret : ret;