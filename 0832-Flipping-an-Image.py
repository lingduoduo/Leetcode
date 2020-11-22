class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(A[0]) for _ in range(len(A))]
        for i in range(len(A)):
            res[i] = [1-num for num in A[i][::-1]]
        return res
                