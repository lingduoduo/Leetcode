class Solution:
    def numTrees(self, n: int) -> int:
        self.d = {}
        return self.dfs(n)


    def dfs(self, n):
        if n in self.d:
            return self.d[n]
        if n == 0 or n == 1:
            return 1
        
        res = 0
        for i in range(1, n+1):
            res += self.dfs(i-1) * self.dfs(n-i)
        self.d[n] = res
        return res

class Solution:
    def numTrees(self, n: int) -> int:
        res = [0] * (n + 1)
        
        res[0] = res[1] = 1
        
        for i in range(2, n + 1):
            tmp = 0
            for j in range(0, i):
                tmp += res[j] * res[i - 1 - j]
            res[i] = tmp
            
        return res[n]

        
        