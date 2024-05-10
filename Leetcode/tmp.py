from typing import List, Optional
import heapq
from collections import defaultdict


# Definition for a Node.
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0

        while i < len(firstList) and j < len(secondList):
            x1, y1 = firstList[i]
            x2, y2 = secondList[j]

            left = max(x1, x2)
            right = min(y1, y2)

            if left <= right:
                res.append([left, right])
            
            if y1 < y2:
                i += 1
            else:
                j += 1
        return res
    
# Test the code        
if __name__ == '__main__':
    res = Solution().intervalIntersection(firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]])
    print(res)
