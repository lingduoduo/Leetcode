class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        def pow(aa, bb):
            if bb == 0 or aa == 1:
                return 1
            if bb == 1:
                return aa
            half = pow(aa, bb//2)
            return (half * half) % 1337 if bb % 2 == 0 else (half * half * aa) % 1337
        
        res = 1
        for x in b:
            res = pow(res, 10) * pow(a, x) % 1337
        return res
    
if __name__ == '__main__':
    res = Solution().superPow(2, [11])
    print(res)