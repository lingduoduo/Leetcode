class Solution:
    def guessNumber(self, n: int) -> int:
        left = 0
        right = n
        
        while left <= right:
            mid = left + (right - left)//2
            ret = guess(mid)
            
            if ret == 0:
                return mid
            elif ret == 1:
                left = mid + 1
            else:
                right = mid - 1
        