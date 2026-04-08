from collections import defaultdict
from typing import List
import math
import heapq

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        heap = []
        for i in range(len(matrix)):
            heapq.heappush(heap, (matrix[i][0], i, 0))
        
        for idx in range(k):
            
            val, i, j = heapq.heappop(heap)
            print(idx, val, i, j)
            if j + 1 < len(matrix[i]):
                heapq.heappush(heap, (matrix[i][j + 1], i, j + 1))
        return val



if __name__ == "__main__":
    res = Solution().kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8)
    print(res)
