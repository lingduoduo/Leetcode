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


if __name__ == "__main__":
    result = Solution().addStrings('198', '23')
    print(result)
