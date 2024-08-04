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


class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        num = 0
        sign = 1  
        curr = 0  

        for chr in s:
            if chr.isdigit():
                num = 10 * num + int(chr)  
            elif chr in "+-":
                curr += sign * num  
                sign = 1 if chr == '+' else -1  
                num = 0  
            elif chr == '(':
                stack.append((sign, curr))
                curr = 0  
                sign = 1 
            elif chr == ')':
                curr += sign * num  
                prev_sign, prev_result = stack.pop()  
                curr = prev_result + prev_sign * curr  
                num = 0 
        curr += sign * num  
        return curr

if __name__ == "__main__":
    s = "(4+5+2)"
    s = "(1 + (4 + 5 + 2) - 3) + (6 + 8)"
    result = Solution().calculate(s)
    print(result)
