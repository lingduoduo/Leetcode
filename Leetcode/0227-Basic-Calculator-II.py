class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        curr = 0
        stack = []
        pre_op = '+'

        for i in range(len(s)):
            if s[i].isdigit():
                curr = curr * 10 + ord(s[i]) - ord('0')
            if s[i] in '+-*/' or i == len(s) - 1:
                if pre_op == '+':
                    stack.append(curr)
                elif pre_op == '-':
                    stack.append(-curr)
                elif pre_op == '*':
                    stack.append(stack.pop() * curr)
                elif pre_op == '/':
                    prev = stack.pop()
                    curr = (-1) * ((-1) * prev // curr) if prev < 0 else prev // curr
                    stack.append(curr)
                pre_op = s[i]
                curr = 0
        return sum(stack)


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        cur = 0
        op = '+'
        for cha in s + "+":
            if cha == " ":
                continue
            elif cha.isdigit():
                cur = cur * 10 + int(cha)
            else:
                if op == "+":
                    stack.append(cur)
                elif op == "-":
                    stack.append(-cur)
                elif op == "*":
                    stack.append(stack.pop() * cur)
                elif op == "/":
                    stack.append(int(stack.pop() / cur))
                cur = 0
                op = cha
        return sum(stack)


# import math
# class Solution:
#     def calculate(self, s: str) -> int:
#         if not s:
#             return 0
#
#         # first define a couple helper methods
#         # operation helper to perform basic math operations
#         def operation(op, second, first):
#             if op == "+":
#                 return first + second
#             elif op == "-":
#                 return first - second
#             elif op == "*":
#                 return first * second
#             elif op == "/":  # integer division
#                 return math.trunc(first / second)
#
#         def precedence(current_op, op_from_ops):
#             if (current_op == "*" or current_op == "/") and (op_from_ops == "+" or op_from_ops == "-"):
#                 return False
#             return True
#
#         nums, ops = [], []
#         i = 0
#         while i < len(s):
#             c = s[i]
#             if c == " ":
#                 continue
#             elif c.isdigit():
#                 num = int(c)
#                 while i < len(s) - 1 and s[i + 1].isdigit():
#                     num = num * 10 + int(s[i + 1])
#                     i += 1
#                 nums.append(num)
#             elif c in ["+", "-", "*", "/"]:
#                 while len(ops) != 0 and precedence(c, ops[-1]):
#                     nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
#                 ops.append(c)
#             i += 1
#
#         while len(ops) > 0:
#            nums.append(operation(ops.pop(), nums.pop(), nums.pop()))
#
#         return nums.pop()



if __name__ == '__main__':
    ###result = Solution().calculate("3+2*2")
    ###print(result)
    ###result = Solution().calculate("3/2")
    ###print(result)
    result = Solution().calculate("14-3/2")
    print(result)
    ###result = Solution().calculate("3/2")
    ###print(result)
