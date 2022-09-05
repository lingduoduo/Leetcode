class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = list(num1)
        l2 = list(num2)
        
        result = []
        lead = 0
        while len(l1) > 0 and len(l2) > 0:
            val = ord(l1.pop()) - ord('0') + ord(l2.pop()) - ord('0') + lead
            if val >= 10:
                lead = 1
                result.append(str(val % 10))
            else:
                lead = 0
                result.append(str(val))
        while len(l1) > 0:
            val = ord(l1.pop()) - ord('0') + lead
            if val >= 10:
                lead = 1
                result.append(str(val % 10))
            else:
                lead = 0
                result.append(str(val))
        while len(l2) > 0:
            val = ord(l2.pop()) - ord('0') + lead
            if val >= 10:
                lead = 1
                result.append(str(val % 10))
            else:
                lead = 0
                result.append(str(val))
        if lead == 1:
            result.append()
        return ''.join(result[::-1])

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        def add(x, y, carry):
            s = x + y + carry
            return (s // 10, s % 10)

        ml = max(len(num1), len(num2))
        res = ''
        carry = 0
        num1 = num1.rjust(ml, '0')
        num2 = num2.rjust(ml, '0')
        for i in range(ml - 1, -1, -1):
            carry, s = add(int(num1[i]), int(num2[i]), carry)
            res = str(s) + res
        return '1' + res if carry else res


if __name__ == "__main__":
    result = Solution().addStrings('198', '23')
    print(result)
