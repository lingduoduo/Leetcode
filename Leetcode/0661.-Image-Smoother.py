class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M or not M[0]:
            return M

        matrix = deepcopy(M)
        for i in range(len(M)):
            for j in range(len(M[0])):
                matrix[i][j] = self.neighbor(M, i, j)
        return matrix

    def neighbor(self, M, x, y):
        idx = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

        cnt = 1
        tot = M[x][y]
        for dx, dy in idx:
            if x + dx < 0 or x + dx >= len(M) or y + dy < 0 or y + dy >= len(M[0]):
                continue
            else:
                cnt += 1
                tot += M[x + dx][y + dy]
        return tot // cnt
