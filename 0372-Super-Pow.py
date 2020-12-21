class Solution:
    def superPow(self, a: int, b) -> int:
        def pow(aa, bb):
            if bb == 0 or aa == 1:
                return 1
            if bb == 1:
                return aa
            half = pow(aa, bb//2)
            return (half * half) % 1337 if bb % 2 == 0 else (half * half * aa) % 1337
        return pow(a, b[0])
        
        # res = 0
        # for i in range(len(b)-1, -1, -1):
        #     res += pow(a, b[i]*10**i)*10**i
        
        # return res % 1337
    
if __name__ == '__main__':
    res = Solution().superPow(2, [11])
    print(res)