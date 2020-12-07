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

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        left = 0 
        res = 0
        while left + 2 < len(arr):
            right = left + 1
            if arr[left] < arr[left + 1]:
                while right + 1 < len(arr) and arr[right] < arr[right + 1]:
                    right += 1
                if right < len(arr) - 1 and arr[right] > arr[right + 1]:
                    while right + 1 < len(arr) and arr[right] > arr[right + 1]:
                        right += 1
                    res = max(res, right - left + 1)
                else:
                    right += 1
            left = right
        return res

if __name__ == '__main__':
    nums = [2, 1, 4, 7, 3, 2, 5]
    nums = [2, 2, 2]
    result = Solution().longestMountain(nums)
    print(result)
