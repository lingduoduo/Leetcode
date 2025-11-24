function numSquares(n: number): number {
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;
    
    for (let i = 1; i <= n; i++) {
        for (let num = 1; num * num <= i; num++) {
            dp[i] = Math.min(dp[i], dp[i - num * num] + 1);
        }
    }
    return dp[n];
};
