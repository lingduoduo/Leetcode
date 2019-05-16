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
