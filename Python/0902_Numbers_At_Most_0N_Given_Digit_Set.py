class Solution:
    def atMostNGivenDigitSet(self, digits, n: int) -> int:
        res = set()
        cnt = len(str(n))

        def dfs(digits, n, path):
            if len(path) > cnt:
                return

            if path:
                curr = int("".join(path))
            else:
                curr = 0

            if curr > n:
                return
            if path and curr <= n:
                res.add(curr)

            for digit in digits:
                dfs(digits, n, path + [digit])

        dfs(digits, n, [])

        return len(res)


class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        S = str(n)
        ls, ld = len(S), len(digits)
        dp = [0] * ls + [1]

        for i in range(ls - 1, -1, -1):
            for d in digits:
                if d < S[i]:
                    dp[i] += ld ** (ls - i - 1)
                elif d == S[i]:
                    dp[i] += dp[i + 1]

        return dp[0] + sum(ld**i for i in range(1, ls))


if __name__ == "__main__":
    # digits = ["1","3","5","7"]
    # n = 100
    # obj = Solution()
    # res = obj.atMostNGivenDigitSet(digits, n)
    # print(res)

    # digits = ["1","4","9"]
    # n = 1000000000
    # obj = Solution()
    # res = obj.atMostNGivenDigitSet(digits, n)
    # print(res)

    # digits = ["7"]
    # n = 8
    # obj = Solution()
    # res = obj.atMostNGivenDigitSet(digits, n)
    # print(res)

    # digits = ["3","4","8"]
    # n = 4
    # obj = Solution()
    # res = obj.atMostNGivenDigitSet(digits, n)
    # print(res)

    digits = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    n = 1597232
    obj = Solution()
    res = obj.atMostNGivenDigitSet(digits, n)
    print(res)
