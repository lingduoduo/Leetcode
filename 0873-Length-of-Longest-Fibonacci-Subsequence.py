class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        if len(A) <= 2:
            return 0
    
        s = set(A)
        n = len(A)
        res = 0
    
        for i in range(n - 1):
            for j in range(i+1, n):
                first = A[i]
                second = A[j]
                count = 2
                while (first + second) in s:
                    count += 1
                    first = second
                    second = first + second
                    if count > res:
                        res = count
        return res
                   