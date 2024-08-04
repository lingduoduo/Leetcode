import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split("=")
        if left[0] == "-":
            left = "0" + left
        if right[0] == "-":
            right = "0" + right
        left = left.replace("-", "+-")
        right = right.replace("-", "+-")
        left_x, left_val, right_x, right_val = 0, 0, 0, 0
        for num in left.split("+"):
            if "x" in num:
                if num == "x":
                    left_x += 1
                elif num == "-x":
                    left_x -= 1
                else:
                    left_x += int(num[:-1])
            else:
                left_val += int(num)
        for num in right.split("+"):
            if "x" in num:
                if num == "x":
                    right_x += 1
                elif num == "-x":
                    right_x -= 1
                else:
                    right_x += int(num[:-1])
            else:
                right_val += int(num)
        left_x -= right_x
        right_val -= left_val
        if left_x != 0 and right_val == 0:
            return "x=0"
        elif left_x != 0 and right_val != 0:
            return "x=" + str(right_val // left_x)
        elif left_x == 0 and right_val == 0:
            return "Infinite solutions"
        elif left_x == 0 and right_val != 0:
            return "No solution"


if __name__ == "__main__":
    equation = "x+5-3+x=6+x-2"
    res = Solution().solveEquation(equation)
    print(res)
