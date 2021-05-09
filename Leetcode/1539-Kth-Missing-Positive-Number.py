class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        num = 1
        n = len(arr)
        for i in range(n):
            while arr[i] != num and k != 0:
                result = num
                num += 1
                k -= 1
            if k == 0:
                return result
            else:
                num += 1
        
        result = num - 1
        while k>0:
            result += 1
            k -= 1


class Solution:
    def findKthPositive(self, arr, k: int) -> int:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = left + (right - left)//2
            if arr[mid] - mid - 1 < k:
                left += 1
            else:
                right -= 1
        return left + k