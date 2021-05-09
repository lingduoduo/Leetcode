class Solution:
    def intervalIntersection(self, A, B):
        i = 0
        j = 0

        res = []

        while i < len(A) and j < len(B):
            x1, y1 = A[i]
            x2, y2 = B[j]
            x = max(x1, x2)
            y = min(y1, y2)
            if x <= y:
                res.append([x, y])
            if y1 < y2:
                i += 1
            else:
                j += 1
        return res

if __name__ == '__main__':
    A = [[0,2],[5,10],[13,23],[24,25]]
    B = [[1,5],[8,12],[15,24],[25,26]]
    results = Solution().intervalIntersection(A, B)
    print(results)





# nput: A = [[0,2],[5,10],[13,23],[24,25]], B = [[1,5],[8,12],[15,24],[25,26]]
# Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]