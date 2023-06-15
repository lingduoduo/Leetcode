# class Solution(object):
#     def change(self, amount, coins):
# dp = [1] + [0] * amount

# for i in range(len(coins)):
#     for j in range(1, amount + 1):
#         if coins[i] <= j:
#             dp[j] += dp[j - coins[i]]


# return dp[-1]


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
