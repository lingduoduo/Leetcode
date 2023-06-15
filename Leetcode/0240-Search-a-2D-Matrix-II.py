class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        import numpy as np

        matrix = np.reshape(matrix, [1, -1])
        return target in matrix

        nums = []
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                nums.append(matrix[i][j])
        return target in nums

        if not matrix or not matrix[0]:
            return False

        nrow = len(matrix)
        ncol = len(matrix[0])

        i = 0
        j = ncol - 1
        while i >= 0 and i < nrow and j >= 0 and j < ncol:
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
        return False
