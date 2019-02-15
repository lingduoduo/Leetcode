class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(matrix)
        cols = len(matrix[0])

        from heapq import heappush, heappop

        heap = list()
        for row in range(rows):
            for col in range(cols):
                heappush(heap, matrix[row][col])

        ordered =[]
        while heap:
            ordered.append(heappop(heap))

        return ordered[k-1]
