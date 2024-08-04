class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack, res = [-1], 0
        for i, e in enumerate(s):
            if e == "(":
                stack.append(i)
            elif e == ")":  
                stack.pop()
                if not stack:  
                    stack.append(i)
                else:
                    res = max(res, i - stack[-1])  
        return res

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left = 0
        right = 0
        res = 0

        # Scan from left to right
        for char in s:
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                res = max(res, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0

        # Scan from right to left
        for char in reversed(s):
            if char == '(':
                left += 1
            else:
                right += 1

            if left == right:
                res = max(res, 2 * left)
            elif left > right:
                left = right = 0

        return res

