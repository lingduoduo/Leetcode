class Solution:
    def convertToTitle(self, n: int) -> str:
        result = ""
        num = n
        
        while num:
            result += chr( (num-1) % 26 + ord("A") )
            num = (num - 1 ) // 26
        return result[::-1]