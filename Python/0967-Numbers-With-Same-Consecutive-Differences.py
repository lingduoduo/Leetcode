class Solution(object):
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """

        if N == 1:
            return [_ for _ in range(0, 10)]

        result = list()
        for i in range(1, 10):
            self.dfs(N - 1, K, i, result)
        return list(set(result))

    def dfs(self, N, K, cur, result):
        if N == 0:
            result.append(cur)
            return result
        l = cur % 10
        if l + K <= 9:
            self.dfs(N - 1, K, cur * 10 + l + K, result)
        if l - K >= 0:
            self.dfs(N - 1, K, cur * 10 + l - K, result)
