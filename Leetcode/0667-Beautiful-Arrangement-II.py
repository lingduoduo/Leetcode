class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        res = list(range(1, 1 + n))
        for i in range(1, k):
            res[i:] = res[:i-1:-1] 
        return res


