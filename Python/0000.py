from typing import List, Optional
from collections import deque, defaultdict, Counter
import heapq

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                d[i+j].append(mat[i][j])

        res = []
        for k, v in d.items():
            if k % 2 == 0:
                res += v[::-1]
            else:
                res += v
        return res

        
                




if __name__ == "__main__":
    res = Solution().findDiagonalOrder(mat = [[1,2,3],[4,5,6],[7,8,9]])
    print(res)
