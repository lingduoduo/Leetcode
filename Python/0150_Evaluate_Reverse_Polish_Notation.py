from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in list("+-*/"):
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    stack.append(num1 + num2)
                elif token == "-":
                    stack.append(num2 - num1)
                elif token == "*":
                    stack.append(num1 * num2)
                elif token == "/":
                    stack.append(int(float(num2) / num1))
            else:
                stack.append(int(token))
        return stack.pop()


from operator import add, sub, mul


class Solution:
    op_map = {"+": add, "-": sub, "*": mul, "/": lambda x, y: int(x / y)}

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in {"+", "-", "*", "/"}:
                stack.append(int(token))
            else:
                op2 = stack.pop()
                op1 = stack.pop()
                stack.append(self.op_map[token](op1, op2))  # 第一个出来的在运算符后面
        return stack.pop()


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for item in tokens:
            if item not in {"+", "-", "*", "/"}:
                stack.append(item)
            else:
                first_num, second_num = stack.pop(), stack.pop()
                stack.append(
                    int(eval(f"{second_num} {item} {first_num}"))
                )
        return int(stack.pop())
