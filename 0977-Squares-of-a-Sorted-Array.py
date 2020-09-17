class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        res = []
        for num in A:
            res.append(num*num)
        res.sort()
        return res