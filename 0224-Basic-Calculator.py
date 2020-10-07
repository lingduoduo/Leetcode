# class Solution(object):
#     def calculate(self, s):
#         """
#         :type s: str
#         :rtype: int
#         """
        
#         stack = []
#         res = 0
#         curr = 0
#         sign = 1
        
#         i = 0
#         for i in range(len(s)):
#             print([res, curr])
#             if s[i] == '(':
#                 stack.append(res)
#                 stack.append(sign)
#                 res = 0
#                 sign = 1
#             elif s[i] == ')':
#                 res += curr * sign
#                 curr = 0
#                 res *= stack.pop()
#                 res += stack.pop()
#             elif s[i].isdigit():
#                 curr = curr * 10 + ord(s[i]) - ord('0')
#             elif s[i] == '+':
#                 res += curr * sign
#                 curr = 0
#                 sign = 1
#             elif s[i] == '-':
#                 res += curr * sign
#                 curr = 0
#                 sign = -1
#         res += curr * sign
#         return res

class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign = 0, 0, 1
        stack = []
        for c in s:
            if c.isdigit():
                num = 10 * num + int(c)
            elif c == "+" or c == "-":
                res = res + sign * num
                num = 0
                sign = 1 if c == "+" else -1
            elif c == "(":
                stack.append(res)
                stack.append(sign)
                res = 0
                sign = 1
            elif c == ")":
                res = res + sign * num
                num = 0
                res *= stack.pop()
                res += stack.pop()
        res = res + sign * num
        return res


if __name__ == '__main__':
    s = '(4+5+2)'
    s = '(1 + (4 + 5 + 2) - 3) + (6 + 8)'
    result = Solution().calculate(s)
    print(result)
