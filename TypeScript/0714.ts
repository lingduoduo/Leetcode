function maxProfit(prices: number[], fee: number): number {
    const n = prices.length;
    const dp: number[][] = Array.from({ length: n }, () => Array(2).fill(0));
    dp[0][0] = -prices[0]; 
    for (let i = 1; i < n; i++) {
        dp[i][0] = Math.max(dp[i - 1][0], dp[i - 1][1] - prices[i]);
        dp[i][1] = Math.max(dp[i - 1][1], dp[i - 1][0] + prices[i] - fee);
    }
    return Math.max(dp[n - 1][0], dp[n - 1][1]);
};
