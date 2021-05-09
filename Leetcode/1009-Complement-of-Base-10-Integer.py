class Solution:
    def bitwiseComplement(self, N: int) -> int:
        res = []
        while N > 0:
            res.append( 1 - N %2)
            N = N //2
        res = res[::-1]
        print(res)

        output = 0
        for i in range(len(res)):
            output = output*2 + res[i]
        return output

if __name__ == '__main__':
    results = Solution().bitwiseComplement(10)
    print(results)