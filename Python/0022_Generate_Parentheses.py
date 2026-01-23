from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(res, n, n, "")
        return res

    def dfs(self, res, left, right, path):
        if left == 0 and right == 0:
            res.append(path)
            return
        if right < left:
            return
        if left > 0:
            self.dfs(res, left - 1, right, path + "(")
        if right > 0:
            self.dfs(res, left, right - 1, path + ")")


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(S=[], left=0, right=0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            if left < n:
                S.append("(")
                backtrack(S, left + 1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right + 1)
                S.pop()

        backtrack()
        return ans

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = [""]

        for k in range(1, n + 1):
            cur = []
            for i in range(k):  # i pairs go inside the first ()
                for inside in dp[i]:
                    print(f"inside: {inside}")
                    for outside in dp[k - 1 - i]:
                        print(f"outsid: {outside}")
                        cur.append("(" + inside + ")" + outside)
            dp[k] = cur

        return dp[n]


if __name__ == "__main__":
    results = Solution().generateParenthesis(1)
    print(results)
