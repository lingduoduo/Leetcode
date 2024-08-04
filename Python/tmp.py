def solution(A):
    MOD = 1_000_000_000
    n = len(A)

    if n < 2:
        return 0

    dp = [0] * n
    min_price = 0
    dp[0] = A[0]

    for i in range(1, n):
        min_price = min(min_price, A[i])
        dp[i] = max(dp[i - 1], A[i] - min_price)

    max_profit = dp[-1]

    for i in range(1, n):
        min_price = A[i]
        for j in range(i + 1, n):
            min_price = min(min_price, A[j])
            dp[j] = max(dp[j], dp[i - 1] + (A[j] - min_price))
            max_profit = max(max_profit, dp[j])

    return max_profit % MOD


# Examples
print(solution([4, 1, 2, 3]))  # Output: 6
print(solution([1, 2, 3, 3, 2, 1, 5]))  # Output: 7
print(solution([1000000000, 1, 2, 2, 1000000000, 1, 1000000000]))  # Output: 999999998
