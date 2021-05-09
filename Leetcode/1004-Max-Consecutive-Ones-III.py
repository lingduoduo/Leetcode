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