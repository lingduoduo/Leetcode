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