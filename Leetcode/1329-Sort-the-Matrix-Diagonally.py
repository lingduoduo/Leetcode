class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        d = collections.defaultdict(list)
        n, m = len(mat), len(mat[0])
        for i in range(n):
            for j in range(m):
                heapq.heappush(d[i - j], mat[i][j])
        for i in range(n):
            for j in range(m):
                mat[i][j] = heapq.heappop(d[i - j])
        return mat         