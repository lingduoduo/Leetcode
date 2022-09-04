class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num is None:
            return ""
        if num == 0:
            return "0"
        
        result = ""
        sign = ""
        if num < 0:
            sign = "-"
            num = -num
        while num > 0:
            result = str(num % 7) + result
            num = int(num / 7)
        result = sign + result
        return result

class Solution:
    def convertToBase7(self, num: int) -> str:
        res = []
        flag = 1 if num < 0 else 0
        num = -num if num < 0 else num
        while num:
            res.append(str(num % 7))
            num = num // 7
        s = ''.join(res[::-1])
        return s if flag == 0 else '-' + s

if __name__ == "__main__":
    s = -8
    result = Solution().convertToBase7(s)
    print(result)
