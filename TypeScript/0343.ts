function integerBreak(n: number): number {
    const dp: number[] = new Array(n + 1).fill(1);
    for (let i = 2; i <= n; i++) {
        for (let j = 1; j <= Math.floor(i / 2); j++) {
            dp[i] = Math.max(dp[i], Math.max(j, dp[j]) * Math.max(i - j, dp[i - j]));
        }
    }
    return dp[n];
};

