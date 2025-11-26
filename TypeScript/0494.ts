function findTargetSumWays(nums: number[], target: number): number {
    const n = nums.length;

    // dp[i] = Map<sum, ways>
    const dp: Map<number, number>[] = Array.from({ length: n + 1 }, () => new Map());

    dp[0].set(0, 1);   // base case

    for (let i = 0; i < n; i++) {
        const num = nums[i];

        // iterate: for each (k, v) in dp[i]
        for (const [k, v] of dp[i]) {
            dp[i + 1].set(k + num, (dp[i + 1].get(k + num) ?? 0) + v);
            dp[i + 1].set(k - num, (dp[i + 1].get(k - num) ?? 0) + v);
        }
    }

    return dp[n].get(target) ?? 0;
}

