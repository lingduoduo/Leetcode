class Solution:
    def checkValidString(self, s: str) -> bool:
        min_op = 0
        max_op = 0

        for c in s:
            if c == "(":
                min_op += 1
            else:
                min_op -= 1

            if c == "(" or c == "*":
                max_op += 1
            else:
                max_op -= 1

            if max_op < 0:
                return False

            min_op = max(0, min_op)

        return min_op == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        lo = hi = 0
        for ch in s:
            if ch == '(':
                lo += 1; hi += 1
            elif ch == ')':
                lo -= 1; hi -= 1
            else:  # '*'
                lo -= 1      # treat as ')'
                hi += 1      # treat as '('

            if hi < 0:
                return False
            if lo < 0:
                lo = 0

        return lo == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for i, c in enumerate(s):
            if c == "(":
                s1.append(i)
            elif c == "*":
                s2.append(i)
            else:
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False

        while s1 and s2:
            if s1[-1] > s2[-1]:  # ( is closer to the end than *
                return False
            s1.pop()
            s2.pop()
        return s1 == []
