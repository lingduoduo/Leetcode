function coinChange(coins: number[], amount: number): number {
    const dp: number[] = new Array(amount + 1).fill(Infinity);
    dp[0] = 0;
    coins.sort((a, b) => a - b);
    for (let i = 1; i <= amount; i++) {
        for (const coin of coins) {
            if (i < coin) {
                break;
            }
            dp[i] = Math.min(dp[i], dp[i - coin] + 1);
        }
    }
    return dp[amount] === Infinity ? -1 : dp[amount];
};
