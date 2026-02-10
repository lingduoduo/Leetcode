from typing import List


from typing import List

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        m1, n1 = len(mat1), len(mat1[0])
        m2, n2 = len(mat2), len(mat2[0])
        if n1 != m2:
            return []

        res = [[0] * n2 for _ in range(m1)]
        row2 = [[] for _ in range(m2)]
        for r in range(m2):
            for c in range(n2):
                v = mat2[r][c]
                if v != 0:
                    row2[r].append((c, v))

        for i in range(m1):
            for k in range(n1):          # shared dimension
                a = mat1[i][k]
                if a == 0:
                    continue
                for j, b in row2[k]:     # mat2 row k -> columns j
                    res[i][j] += a * b

        return res
