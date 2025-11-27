class Solution(object):
    def __init__(self):
        self.lessThan20 = [
            "",
            "One",
            "Two",
            "Three",
            "Four",
            "Five",
            "Six",
            "Seven",
            "Eight",
            "Nine",
            "Ten",
            "Eleven",
            "Twelve",
            "Thirteen",
            "Fourteen",
            "Fifteen",
            "Sixteen",
            "Seventeen",
            "Eighteen",
            "Nineteen",
        ]
        self.tens = [
            "",
            "Ten",
            "Twenty",
            "Thirty",
            "Forty",
            "Fifty",
            "Sixty",
            "Seventy",
            "Eighty",
            "Ninety",
        ]
        self.thousands = ["", "Thousand", "Million", "Billion"]

    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        res = ""
        for i in range(len(self.thousands)):
            if num % 1000 != 0:
                res = self.helper(num % 1000) + self.thousands[i] + " " + res
            num = num // 1000
        return res.strip()

    def helper(self, num):
        if num == 0:
            return ""
        if num < 20:
            return self.lessThan20[num] + " "
        if num < 100:
            return self.tens[num // 10] + " " + self.helper(num % 10)
        else:
            return self.lessThan20[num // 100] + " Hundred " + self.helper(num % 100)


class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
        tens = ["", "Ten", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        teens = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen","Nineteen"]
        suffixes = ["", "Thousand", "Million", "Billion", "Trillion", "Quadrillion", "Quintillion", "Sextillion","Septillion", "Octillion", "Nonillion", "Decillion"]

        words = []
        i = 0
        while num > 0:
            triplet = num % 1000
            num = num // 1000
            if triplet == 0:
                i += 1
                continue
            curr = []
            if triplet // 100 > 0:
                curr.append(ones[triplet // 100])
                curr.append("Hundred")
            if triplet % 100 >= 10 and triplet % 100 <= 19:
                curr.append(teens[triplet % 10])
            else:
                if triplet % 100 >= 20:
                    curr.append(tens[triplet % 100 // 10])
                if triplet % 10 > 0:
                    curr.append(ones[triplet % 10])
            if i > 0:
                curr.append(suffixes[i])
            words = curr + words
            i += 1
        return " ".join(words)