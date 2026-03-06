class Solution:
    def numberOfPatterns(self, m: int, n: int) -> int:
        skip = [[0] * 10 for _ in range(10)]
        
        skip[1][3] = skip[3][1] = 2
        skip[1][7] = skip[7][1] = 4
        skip[3][9] = skip[9][3] = 6
        skip[7][9] = skip[9][7] = 8
        skip[1][9] = skip[9][1] = 5
        skip[3][7] = skip[7][3] = 5
        skip[4][6] = skip[6][4] = 5
        skip[2][8] = skip[8][2] = 5

        visited = [False] * 10

        def dfs(cur: int, len: int) -> int:
            if len > n:
                return 0

            res = 1 if m <= len <= n else 0
            visited[cur] = True

            for nxt in range(1, 10):
                mid = skip[cur][nxt]
                if not visited[nxt] and (mid == 0 or visited[mid]):
                    res += dfs(nxt, len + 1)

            visited[cur] = False
            return res

        return dfs(1, 1) * 4 + dfs(2, 1) * 4 + dfs(5, 1)