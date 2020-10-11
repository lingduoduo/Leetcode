class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int):
        matrix = [ (i, j) for i in range(R) for j in range(C) ]
        d = {}
        for i in range(len(matrix)):
            r, c = matrix[i]
            d[(r, c)] = abs(r-r0) + abs(c-c0)
        res = []
        results= sorted(d.items(), key=lambda x: x[1])
        for k, v in results:
            res.append(k)
        return res

if __name__ == '__main__':
    R = 1
    C = 2
    r0 = 0
    c0 = 0
    res = []
    results = Solution().allCellsDistOrder(R, C, r0, c0)
    print(results)
    
