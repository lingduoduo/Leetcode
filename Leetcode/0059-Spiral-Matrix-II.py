class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ###res = [[0] * n for _ in range(n)]
        ###rowstart = 0
        ###rowend = n - 1
        ###colstart = 0
        ###colend = n - 1
        ###step = 1
        ###while rowstart < rowend and colstart < colend:
        ###    for j in range(colstart, colend):
        ###        res[rowstart][j] = step
        ###        step += 1
        ###    for i in range(rowstart, rowend):
        ###        res[i][colend] = step
        ###        step += 1
        ###    for j in range(colend, colstart, -1):
        ###        res[rowend][j] = step
        ###        step += 1
        ###    for i in range(rowend, rowstart, -1):
        ###        res[i][colstart] = step
        ###        step += 1
        ###    rowstart += 1
        ###    rowend -= 1
        ###    colstart += 1
        ###    colend -= 1
        ###if rowstart == rowend and colstart == colend:
        ###    res[rowstart][colstart] = step
        ###    step += 1

        ###return res

        matrix = []
        for i in range(n):
            matrix.append([0 for i in range(n)])

        rowBegin = 0
        rowEnd = n - 1
        colBegin = 0
        colEnd = n - 1
        num = 1

        while rowBegin <= rowEnd and colBegin <= colEnd:
            for i in range(colBegin, colEnd + 1):
                matrix[rowBegin][i] = num
                num += 1
            rowBegin += 1

            for i in range(rowBegin, rowEnd + 1):
                matrix[i][colEnd] = num
                num += 1
            colEnd -= 1

            if rowBegin <= rowEnd:
                for i in range(colEnd, colBegin - 1, -1):
                    matrix[rowEnd][i] = num
                    num += 1
                rowEnd -= 1

            if colBegin <= colEnd:
                for i in range(rowEnd, rowBegin - 1, -1):
                    matrix[i][colBegin] = num
                    num += 1
                colBegin += 1
        return matrix

    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        curx = cury = curd = 0
        for i in range(1, n * n + 1):
            res[curx][cury] = i
            newx, newy = curx + directions[curd][0], cury + directions[curd][1]
            if newx < 0 or newx >= n or newy < 0 or newy >= n or res[newx][newy]:
                curd = (curd + 1) % 4
            curx += directions[curd][0]
            cury += directions[curd][1]
        return res


if __name__ == "__main__":
    result = Solution().generateMatrix(4)
    print(result)
