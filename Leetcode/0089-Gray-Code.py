class Solution:
    def grayCode(self, n: int):
        ###return map(lambda x: int(x, 2), self.recursive_loop(n))

        s = self.recursive_loop(n)
        res = []
        for i in range(len(s)):
            tmp = 0
            for cha in s[i]:
                tmp = tmp*2 + (cha=='1')
            res.append(tmp)
        return res

    def recursive_loop(self, n):
        res = None
        if n == 1:
            res = ['0', '1']
        else:
            prev = self.recursive_loop(n-1)
            res = ['0' + x for x in prev] + ['1' + x for x in prev[::-1]] 
        return res

if __name__ == '__main__':
    n = 3
    results = Solution().recursive_loop(n)
    print(results)