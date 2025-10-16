function maxSubArray(nums: number[]): number {
    const n = nums.length;
    if (n === 0) return 0;

    const dp: number[] = new Array(n);
    dp[0] = nums[0];
    let res = dp[0];

    for (let i = 1; i < n; i++) {
        dp[i] = Math.max(nums[i], dp[i - 1] + nums[i]);
        res = Math.max(res, dp[i]);
    }

    return res;
}