class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for idx, num in enumerate(A):
            if abs(num - idx) > 1:
                return False
        return True
