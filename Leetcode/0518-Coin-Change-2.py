from typing import List


class Solution(object):
    def change(self, amount, coins):
        self.res = set()
        self.dfs(amount, coins, [])
        return len(self.res)

    def dfs(self, amount, coins, path):
        if amount < 0:
            return

        if amount == 0:
            self.res.add(tuple(sorted(path)))

        for i in range(len(coins)):
            self.dfs(amount - coins[i], coins, path + [coins[i]])


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]

        return dp[0][amount]


if __name__ == "__main__":
    # amount = 5
    # coins = [1, 2, 5]
    # res = Solution().change(amount, coins)
    # print(res)

    # amount = 3
    # coins = [2]
    # res = Solution().change(amount, coins)
    # print(res)

    amount = 10
    coins = [10]
    res = Solution().change(amount, coins)
    print(res)
