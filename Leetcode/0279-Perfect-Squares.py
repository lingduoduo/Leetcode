import math


class Solution:
    def numSquares(self, n: int) -> int:
        square_nums = [i**2 for i in range(0, int(math.sqrt(n)) + 1)]

        dp = [float("inf")] * (n + 1)
        # bottom case
        dp[0] = 0

        for i in range(1, n + 1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)

        return dp[-1]


from collections import deque


class Solution:
    def numSquares(self, n: int) -> int:
        q = deque()
        q.append(n)
        count = 0
        while q:
            _q = set()
            for _ in range(len(q)):
                target = q.popleft()
                if target == 0:
                    return count
                i = 1
                while i**2 <= target:
                    rest = target - i**2
                    _q.add(rest)
                    i += 1
            count += 1
            q = deque(_q)


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):  # 遍历背包
            for j in range(1, int(i**0.5) + 1):  # 遍历物品
                # 更新凑成数字 i 所需的最少完全平方数数量
                dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]
