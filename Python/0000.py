from collections import defaultdict, deque
from typing import List
import math
import heapq
import bisect 


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])

        l, r = 0, row * col
        while l < r:
            m = l + (r - l)//2
            mr = m // col
            mc = m % col
            if matrix[mr][mc] == target:
                return True
            elif matrix[mr][mc] < target:
                l = m + 1
            else:
                r = m
        return False

if __name__ == "__main__":
    print(Solution().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))
