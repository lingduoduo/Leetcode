class Solution:
    def maxSubarraySumCircular(self, A: List[int]) -> int:
        max_loc = max_glo = min_loc = min_glo = A[0]
        for num in A[1:]:
            max_loc = max(num, max_loc + num)
            max_glo = max(max_glo, max_loc)
            min_loc = min(num, min_loc + num)
            min_glo = min(min_glo, min_loc)
        s = sum(A)
        if s == min_glo:
            return max_glo
        else:
            return max(max_glo, s-min_glo)
            