class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        num = columnNumber
        
        while num:
            result += chr( (num-1) % 26 + ord("A") )
            num = (num - 1 ) // 26
        return result[::-1]