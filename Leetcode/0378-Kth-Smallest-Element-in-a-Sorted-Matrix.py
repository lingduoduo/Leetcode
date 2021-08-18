# class Solution(object):
#     def kthSmallest(self, matrix, k):
"""
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        ###rows = len(matrix)
        ###cols = len(matrix[0])
        #
        ###from heapq import heappush, heappop
        #
        ###heap = list()
        ###for row in range(rows):
        ###    for col in range(cols):
        ###        heappush(heap, matrix[row][col])
        #
        ###ordered =[]
        ###while heap:
        ###    ordered.append(heappop(heap))
        #
        ###return ordered[k-1]
        
        ###Seond Try
       # left = matrix[0][0]
       # right = matrix[-1][-1]
        
       # while left < right:
       #     mid = left + (right - left) // 2
       #     tot = 0
       #     for row in matrix:
       #         tot += self.upperBound(row, mid)
       #     if tot < k:
       #         left = mid + 1
       #     else:
       #         right = mid
       # return left
    
    # def upperBound(self, nums, target):
    #    """
    #    return index such that target<nums[index]
    #    """
    #    if not nums:
    #        return -1
        
    #    left = 0
    #    right = len(nums)
        
    #    while left < right:
    #        mid = left + (right - left) // 2
    #        if nums[mid] <= target:
    #            left = mid + 1
    #        else:
    #            right = mid
    #    return left

        # left = matrix[0][0]
        # right = matrix[-1][-1]

        # while left<right:
        #     mid = left + (right-left)//2
        #     position = sum(bisect.bisect_right(row, mid) for row in matrix)

        #     if position<k:
        #         left=mid+1
        #     else:
        #         right=mid
        # return left

# from typing import List
# import heapq
# import itertools
# class Solution:
#     def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
#         nums = list(itertools.chain(*matrix))
#         heapq.heapify(nums)
#         for i in range(k):
#             res = heapq.heappop(nums)
#         return res

from typing import List
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        m = len(matrix)
        n = len(matrix[0])
        l = matrix[0][0]
        r = matrix[m-1][n-1]

        while l <= r:
            mid = l + (r - l)//2
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

if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    result = Solution().kthSmallest(matrix, k)
    print(result)
