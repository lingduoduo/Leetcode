class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        res = [[0] * n for _ in range(n)]
        rowstart = 0
        rowend = n - 1
        colstart = 0
        colend = n - 1
        step = 1
        while rowstart < rowend and colstart < colend:
            for j in range(colstart, colend):
                res[rowstart][j] = step
                step += 1
            for i in range(rowstart, rowend):
                res[i][colend] = step
                step += 1
            for j in range(colend, colstart, -1):
                res[rowend][j] = step
                step += 1
            for i in range(rowend, rowstart, -1):
                res[i][colstart] = step
                step += 1
            rowstart+=1
            rowend-=1
            colstart+=1
            colend-=1
        if rowstart == rowend and colstart == colend:
            res[rowstart][colstart] = step
            step += 1

        return res

if __name__ == '__main__':
    result = Solution().generateMatrix(4)
    print(result)
