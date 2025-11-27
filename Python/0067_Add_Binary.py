class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        if len(a) < len(b):
            a = "0" * (len(b) - len(a)) + a
        else:
            b = "0" * (len(a) - len(b)) + b
        stack1 = list(a)
        stack2 = list(b)
        result = ""
        carry = 0
        while stack1 and stack2:
            s1, s2 = stack1.pop(), stack2.pop()
            curr = int(s1) + int(s2) + carry
            if curr >= 2:
                carry = 1
                curr = curr % 2
            else:
                carry = 0
            result = str(curr) + result
        if carry == 1:
            result = "1" + result
        return result


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry, val = "", 0, 0
        for i in range(max(len(a), len(b))):
            val = carry
            if i < len(a):
                val += int(a[-(i + 1)])
            if i < len(b):
                val += int(b[-(i + 1)])
            carry, val = val // 2, val % 2
            result += str(val)
        if carry == 1:
            result = result + str(carry)
        return result[::-1]


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        def add(x, y, carry):
            s = x + y + carry
            return (s // 2, s % 2)

        ml = max(len(a), len(b))
        res = ""
        carry = 0
        a = a.rjust(ml, "0")
        b = b.rjust(ml, "0")
        for i in range(ml - 1, -1, -1):
            carry, s = add(int(a[i]), int(b[i]), int(carry))
            res = str(s) + res
        return "1" + res if carry else res
