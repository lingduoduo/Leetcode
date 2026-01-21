from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math

class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        abs_tot = 0
        neg_cnt = 0
        min_v = float("inf")

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                abs_tot += abs(matrix[i][j])
                if matrix[i][j] < 0: neg_cnt += 1
                min_v = min(min_v, abs(matrix[i][j]))
        
        if neg_cnt % 2 != 0:
            abs_tot -= 2 * min_v
        
        return abs_tot



if __name__ == "__main__":
    res = Solution().maxMatrixSum(matrix = [[1,2,3],[-1,-2,-3],[1,2,3]])
    print(res)

