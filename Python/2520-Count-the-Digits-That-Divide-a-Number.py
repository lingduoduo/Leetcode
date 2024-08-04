class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        number = num
        while num:
            digit = num % 10
            num = num // 10
            res += 1 if number % digit == 0 else 0
        return res
