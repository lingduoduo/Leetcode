class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        prev = -1
        while n > 0:
            curr = n % 2
            if prev >= 0 and curr != (1+prev)%2:
                return False
            else:
                prev = curr
            n = n//2
        return True