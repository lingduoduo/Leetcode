class Solution(object):
    def longestMountain(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = [0] * len(A)
        right = [0] * len(A)
        
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                left[i] = left[i - 1] + 1
        
        for i in range(len(A) - 2, -1, -1):
            if A[i] > A[i + 1]:
                right[i] = right[i + 1] + 1
        
        res = 0
        for i in range(len(A)):
            if left[i] > 0 and right[i] > 0:
                res = max(res, left[i] + right[i] + 1)
        return res


if __name__ == '__main__':
    nums = [2, 1, 4, 7, 3, 2, 5]
    nums = [2, 2, 2]
    result = Solution().longestMountain(nums)
    print(result)
