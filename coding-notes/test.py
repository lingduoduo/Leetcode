# from typing import List
# import heapq
# class Solution:
#     def getLeastNumbers_Solution(self, nums, k):
#         res = []
#         heapq.heapify(nums)
#         for i in range(k):
#             res.append(heapq.heappop(nums))
#         return res


from typing import List
import heapq
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        nums = [matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))]
        print(nums)

        heapq.heapify(nums)
        for i in range(k):
            res = heapq.heappop(nums)
        return res

if __name__ == '__main__':
    res = Solution().kthSmallest(matrix = [[1,5,9],[10,11,13],[12,13,15]], k = 8)
    print(res)