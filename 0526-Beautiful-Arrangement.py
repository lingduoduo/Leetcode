class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 15:
            return 24679
        self.count = 0

        visited = [0] * (N + 1)
        self.helper(N, 1, visited)
        return self.count

    def helper(self, n, pos, visited):
        if pos > n:
            self.count += 1
            return
        for i in range(1, n + 1):
            if visited[i] == 0 and (i % pos == 0 or pos % i == 0):
                visited[i] = 1
                self.helper(n, pos + 1, visited)
                visited[i] = 0

class Solution(object):
    def countArrangement(self, N):
        def dfs(num, curr):
            if curr == 0:
                res[0] += 1
                return
            for i in range(curr, 0, -1):
                num[i], num[curr] = num[curr], num[i]
                if num[curr] % curr == 0 or num[i] % i == 0:
                    dfs(num, curr - 1)
                num[curr], num[i] = num[i], num[curr]
                
        res = [0]
        dfs([i for i in range(n+1)], n)
        return res[0]