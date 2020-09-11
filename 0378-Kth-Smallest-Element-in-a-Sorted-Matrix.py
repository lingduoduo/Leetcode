class Solution(object):
    def kthSmallest(self, matrix, k):
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
    ###    left = matrix[0][0]
    ###    right = matrix[-1][-1]
        
    ###    while left < right:
    ###        mid = left + (right - left) // 2
    ###        tot = 0
    ###        for row in matrix:
    ###            tot += self.upperBound(row, mid)
    ###        if tot < k:
    ###            left = mid + 1
    ###        else:
    ###            right = mid
    ###    return left
    
    ###def upperBound(self, nums, target):
    ###    """
    ###    return index such that target<nums[index]
    ###    """
    ###    if not nums:
    ###        return -1
        
    ###    left = 0
    ###    right = len(nums)
        
    ###    while left < right:
    ###        mid = left + (right - left) // 2
    ###        if nums[mid] <= target:
    ###            left = mid + 1
    ###        else:
    ###            right = mid
    ###    return left

        left = matrix[0][0]
        right = matrix[-1][-1]

        while left<right:
            mid = left + (right-left)//2
            position = sum(bisect.bisect_right(row, mid) for row in matrix)

            if position<k:
                left=mid+1
            else:
                right=mid
        return left

if __name__ == '__main__':
    matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
    k = 8
    result = Solution().kthSmallest(matrix, k)
    print(result)
