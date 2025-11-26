function canPartition(nums: number[]): boolean {
    let sum = nums.reduce((a, b) => a + b, 0);

    if (sum % 2 !== 0) return false;

    const target = sum / 2;

    // dp[i] = can we make sum i?
    const dp = new Array(target + 1).fill(false);
    dp[0] = true;

    for (const num of nums) {
        for (let i = target; i >= num; i--) {
            dp[i] = dp[i] || dp[i - num];
        }
    }

    return dp[target];
}
