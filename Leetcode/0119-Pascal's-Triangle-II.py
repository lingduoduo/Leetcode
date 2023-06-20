from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = [1] = [0]*rowIndex
        
        for i in range(rowIndex):
            result[0] = 1
            for j in range(i+1, 0, -1):
                result[j] = result[j]+result[j-1]
        return result
            
        