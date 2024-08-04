class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(n):
            reta = retb = 0
            for i in range(len(A)):
                if A[i] != n and B[i] != n:
                    return -1
                if A[i] != n:
                    reta += 1
                elif B[i] != n:
                    retb += 1
            return min(reta, retb)

        res = check(A[0])
        if res != -1 or A[0] == B[0]:
            return res
        return check(B[0])
