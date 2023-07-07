from typing import List


class Solution(object):
    def generateMatrix(self, n):
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


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        loop, mid = n // 2, n // 2  # 迭代次数、n为奇数时，矩阵的中心点
        count = 1  # 计数

        for offset in range(1, loop + 1):  # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - offset):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - offset):  # 从上至下
                nums[i][n - offset] = count
                count += 1
            for i in range(n - offset, starty, -1):  # 从右至左
                nums[n - offset][i] = count
                count += 1
            for i in range(n - offset, startx, -1):  # 从下至上
                nums[i][starty] = count
                count += 1
            startx += 1  # 更新起始点
            starty += 1

        if n % 2 != 0:  # n为奇数时，填充中心点
            nums[mid][mid] = count
        return nums


if __name__ == "__main__":
    result = Solution().generateMatrix(4)
    print(result)
