class Solution:
    def beautifulArray(self, N: int) -> List[int]:
        if N == 1: return [1]
        odd = [i * 2 - 1 for i in self.beautifulArray(N // 2 + N % 2)]
        even = [i * 2 for i in self.beautifulArray(N // 2)]
        return odd + even
        