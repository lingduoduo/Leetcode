from typing import List, Optional
from collections import Counter
import heapq
import re
from collections import deque, defaultdict
from typing import List
import random
import bisect
import math

# class Solution:
    # def maxLength(self, arr: List[str]) -> int:
    #     res = 0
    #     for i in range(len(arr)):
    #         for  j in range(i + 1):
    #             res = max(res, len(set(arr[i] + arr[j])))
    #     return res

from typing import List

class SparseVector:
    def __init__(self, nums: List[int]):
        self.d = {i: v for i, v in enumerate(nums) if v != 0}

    def dotProd(self, vec: "SparseVector") -> int:
        small, large = (self.d, vec.d) if len(self.d) <= len(vec.d) else (vec.d, self.d)
        res = 0
        for k, v in small.items():
            res += v * large.get(k, 0)
        return res


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])

        rows = [SparseVector(mat1[i]) for i in range(m1)]

        cols = []
        for j in range(n2):
            col_j = [mat2[i][j] for i in range(m2)]
            cols.append(SparseVector(col_j))

        res = [[0] * n2 for _ in range(m1)]
        for i in range(m1):
            rvec = rows[i]
            if not rvec.d:
                continue
            for j in range(n2):
                val = rvec.dotProd(cols[j])
                if val:
                    res[i][j] = val
        return res


if __name__ == "__main__":
    res = Solution().generateParenthesis(n=3)
    print(res)




