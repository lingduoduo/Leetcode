class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = [[0]*len(A[0]) for _ in range(len(A))]
        for i in range(len(A)):
            res[i] = [1-num for num in A[i][::-1]]
        return res

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            for i in range((len(row) + 1) // 2):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
        return A