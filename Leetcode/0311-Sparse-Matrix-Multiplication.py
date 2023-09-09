from typing import List


class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])
        res = [[0 for j in range(n2)] for i in range(m1)]
        x = [dict() for i in range(m1)]
        y = [dict() for i in range(n2)]
        for i in range(m1):
            for j in range(n1):
                if mat1[i][j] != 0:
                    x[i][j] = mat1[i][j]
        for i in range(m2):
            for j in range(n2):
                if mat2[i][j] != 0:
                    y[j][i] = mat2[i][j]
        for i in range(m1):
            for j in range(n2):
                for r in x[i]:
                    if r in y[j]:
                        res[i][j] += x[i][r] * y[j][r]
        return res
