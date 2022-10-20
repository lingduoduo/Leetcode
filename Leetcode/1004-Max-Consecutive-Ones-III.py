class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        A.append(2)
        res = 0
        left = 0
        zero = 0
        n = len(A)

        for right in range(n):
            res = max(res, right - left)
            if A[right] == 0:
                zero += 1
            while zero > K:
                if A[left] == 0:
                    zero -= 1
                left += 1
        return res
        
class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        A.append(2)
        left,res,right=0,0,1
        c=A[left:right].count(0)
        while right<len(A):
            if c<=K:
                res=max(res, right-left)
                if A[right]==0:
                    c+=1
                right+=1
            else:
                if A[left]==0:
                    c-=1
                left+=1
        return res

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        for right in range(len(nums)):
            # If we included a zero in the window we reduce the value of k.
            # Since k is the maximum zeros allowed in a window.
            k -= 1 - nums[right]
            # A negative k denotes we have consumed all allowed flips and window has
            # more than allowed zeros, thus increment left pointer by 1 to keep the window size same.
            if k < 0:
                # If the left element to be thrown out is zero we increase k.
                k += 1 - nums[left]
                left += 1
        return right - left + 1