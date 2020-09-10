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