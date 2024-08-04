# class Solution(object):
#     def matrixReshape(self, nums, r, c):
#         """
#         :type nums: List[List[int]]
#         :type r: int
#         :type c: int
#         :rtype: List[List[int]]
#         """
# n = len(nums)
# m = len(nums[0])
# if n == 0 and m == 0:
#     return nums
# if n * m != r * c:
#     return nums
# results = [[0] * c for _ in range(r)]
# for i in range(n * m):
#     nums_i = int(i / m)
#     nums_j = int(i % m)
#     results_r = int(i / c)
#     results_c = int(i % c)
#     results[results_r][results_c] = nums[nums_i][nums_j]
# return results


# if __name__ == "__main__":
#     print(Solution().matrixReshape([[1, 2], [3, 4]], 4, 1))


class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])
        if n == 0 and m == 0:
            return mat
        if n * m != r * c:
            return mat

        res = [[0] * c for _ in range(r)]
        idx = 0
        for i in range(r):
            for j in range(c):
                row, col = divmod(idx, n)
                res[i][j] = mat[row][col]
                idx += 1
        return res


if __name__ == "__main__":
    res = Solution().matrixReshape(mat=[[1, 2], [3, 4]], r=1, c=4)
    print(res)

    res = Solution().matrixReshape(mat=[[1, 2], [3, 4]], r=4, c=1)
    print(res)
