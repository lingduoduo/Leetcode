class Solution:
    def checkValidString(self, s: str) -> bool:
        min_op = 0
        max_op = 0

        for c in s:
            if c == '(':
                min_op += 1
            else:
                min_op -= 1

            if c == '(' or c == '*':
                max_op += 1
            else:
                max_op -= 1

            if max_op < 0:
                return False

            min_op = max(0, min_op)

        return min_op == 0


class Solution:
    def checkValidString(self, s: str) -> bool:
        old_set = set([0])
        for c in s:
            new_set = set()
            if c == '(':
                for t in old_set:
                    new_set.add(t + 1)
            elif c == ')':
                for t in old_set:
                    if t > 0:
                        new_set.add(t - 1)
            elif c == '*':
                for t in old_set:
                    new_set.add(t + 1)
                    new_set.add(t)
                    if t > 0:
                        new_set.add(t - 1)
            old_set = new_set
        return 0 in old_set


class Solution(object):
    def checkValidString(self, s):
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0: break
            lo = max(lo, 0)

        return lo == 0

class Solution:
    def checkValidString(self, s: str) -> bool:
        s1 = []
        s2 = []
        for i, c in enumerate(s):
            if c == '(':
                s1.append(i)
            elif c == '*':
                s2.append(i)
            else:
                if s1:
                    s1.pop()
                elif s2:
                    s2.pop()
                else:
                    return False

        while s1 and s2:
            if s1[-1] > s2[-1]: # ( is closer to the end than *
                return False
            s1.pop()
            s2.pop()
        return s1 == []