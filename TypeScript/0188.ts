function maxProfit(k: number, prices: number[]): number {
    let dp: number[][] = Array.from({ length: k + 1 }, () => [1000, 0]);
    for (let price of prices) {
        for (let i = 1; i <= k; i++) {
            dp[i][0] = Math.min(dp[i][0], price - dp[i - 1][1]);
            dp[i][1] = Math.max(dp[i][1], price - dp[i][0]);
        }
    }
    return k === 0 ? 0 : dp[k][1];
};
