function maxProfit(prices: number[]): number {
    const k = 2;
    const n = prices.length;

    // dp[i][0] = minimum cost for the i-th transaction buy
    // dp[i][1] = max profit for the i-th transaction sell
    const INF = Number.POSITIVE_INFINITY;
    const dp: number[][] = Array.from({ length: k + 1 }, () => [INF, 0]);

    for (const price of prices) {
        for (let i = 1; i <= k; i++) {
            // buy i-th stock (cost = price - previous profit)
            dp[i][0] = Math.min(dp[i][0], price - dp[i-1][1]);

            // sell i-th stock (profit = price - cost)
            dp[i][1] = Math.max(dp[i][1], price - dp[i][0]);
        }
    }

    return dp[k][1];
}
