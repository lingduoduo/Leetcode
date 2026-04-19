class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        if len(s2) == 1:
            for i in range(len(s1)):
                if s1[i] == s2:
                    return s2

        def find_subseq(s):
            t = 0
            while s < len(s1):
                if s1[s] == s2[t]:
                    t += 1
                    if t == len(s2):
                        break
                s += 1
            return s if t == len(s2) else None

        # Improve - Get best starting point of subsequence ending at s1[s]
        def improve_subseq(s):
            t = len(s2) - 1
            while t >= 0:
                if s1[s] == s2[t]:
                    t -= 1
                s -= 1
            return s + 1

        s, min_len, res = 0, float('inf'), ''
        while s < len(s1):
            end = find_subseq(s)  # Find end-point of subsequence
            if not end:
                break
            start = improve_subseq(end)  # Improve start-point of subsequence
            if end - start + 1 < min_len:  # Track min length
                min_len = end - start + 1
                res = s1[start:end + 1]
            s = start + 1  # Start next subsequence search

        return res


class Solution:
    def minWindow(self, s1: str, s2: str) -> str:
        m, n = len(s1), len(s2)
        dp = [[-1] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if s1[i] == s2[j]:
                    dp[i][j] = i if j == 0 else (dp[i - 1][j - 1] if i > 0 else -1)
                else:
                    dp[i][j] = dp[i - 1][j] if i > 0 else -1

        start = -1
        min_len = float("inf")

        for i in range(m):
            if dp[i][n - 1] != -1:
                cur_len = i - dp[i][n - 1] + 1
                if cur_len < min_len:
                    min_len = cur_len
                    start = dp[i][n - 1]

        return "" if start == -1 else s1[start:start + min_len]
                    