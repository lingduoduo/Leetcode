class Solution:
    def addDigits(self, num: int) -> int:
        # if num <= 0:
        #     return 0
        # else:
        #     result = (num - 1) % 9 + 1
        #
        # return result

        while num >= 10:
            s = str(num)
            digits = [int(cha) for cha in s]
            num = sum(digits)
        return num
        
