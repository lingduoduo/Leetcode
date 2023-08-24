from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        l = matrix[0][0]
        r = matrix[m - 1][n - 1]
        while l <= r:
            mid = l + (r - l) // 2
            cnt = 0
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] <= mid:
                        cnt += 1
            if cnt < k:
                l = mid + 1
            else:
                r = mid - 1
        return l


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        q = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            heapq.heappush(q, (matrix[i][0], i, 0))
        for i in range(k):
            num, row, col = heapq.heappop(q)
            if 0 <= col + 1 < n:
                heapq.heappush(q, (matrix[row][col + 1], row, col + 1))
        return num


if __name__ == "__main__":
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    result = Solution().kthSmallest(matrix, k)
    print(result)
