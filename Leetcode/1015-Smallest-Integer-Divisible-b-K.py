class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 2 == 0 or K % 5 == 0:
            return -1
        
        cur, res = 0, 1
        while True:
            cur = (10 * cur + 1) % K
            if cur == 0:
                return res
            res += 1
        return res
        