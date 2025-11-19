function calculateMinimumHP(dungeon: number[][]): number {
    const m = dungeon.length;
    const n = dungeon[0].length;

    // Create dp with an extra row and column
    const dp: number[][] = Array.from({ length: m + 1 }, () =>
        Array(n + 1).fill(Infinity)
    );

    // Base case: the knight needs at least 1 HP right after the princess cell
    dp[m][n - 1] = 1;
    dp[m - 1][n] = 1;

    // Fill DP bottom-up
    for (let i = m - 1; i >= 0; i--) {
        for (let j = n - 1; j >= 0; j--) {
            const need = Math.min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j];
            dp[i][j] = Math.max(1, need);
        }
    }

    return dp[0][0];
}