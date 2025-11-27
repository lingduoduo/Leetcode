from typing import List

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        nums = [[0] * n for _ in range(n)]
        startx, starty = 0, 0  # 起始点
        j, mid = n // 2, n // 2  # 迭代次数、n为奇数时，矩阵的中心点
        count = 1  # 计数

        for offset in range(1, j + 1):  # 每循环一层偏移量加1，偏移量从1开始
            for i in range(starty, n - j):  # 从左至右，左闭右开
                nums[startx][i] = count
                count += 1
            for i in range(startx, n - j):  # 从上至下
                nums[i][n - j] = count
                count += 1
            for i in range(n - j, starty, -1):  # 从右至左
                nums[n - j][i] = count
                count += 1
            for i in range(n - j, startx, -1):  # 从下至上
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
