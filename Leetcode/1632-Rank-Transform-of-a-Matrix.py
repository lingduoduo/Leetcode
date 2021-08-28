import collections
class Solution:
    def matrixRankTransform(self, matrix: List[List[int]]) -> List[List[int]]:
        def find(i):
            if p[i] != i:
                p[i] = find(p[i])
            return p[i]

        n, m = len(matrix), len(matrix[0])
        rank = [0] * (m + n)
        dic = defaultdict(list)
        for i in range(n):
            for j in range(m):
                dic[matrix[i][j]].append([i, j])

        for a in sorted(dic):
            p = list(range(m + n))
            rank2 = rank[:]
            for i, j in dic[a]:
                i, j = find(i), find(j + n)
                p[i] = j 
                rank2[j] = max(rank2[i], rank2[j]) 
            for i, j in dic[a]:
                rank[i] = rank[j + n] = matrix[i][j] = rank2[find(i)] + 1
        return matrix
