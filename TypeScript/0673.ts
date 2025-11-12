function findNumberOfLIS(nums: number[]): number {
    const dp: number[] = new Array(nums.length).fill(1);
    const count: number[] = new Array(nums.length).fill(1);
    for (let i = 0; i < nums.length; i++) {
        for (let j = 0; j < i; j++) {
            if (nums[j] < nums[i]) {
                dp[i] = Math.max(dp[i], dp[j] + 1);
                count[i] = 0;
            } else {
                count[i] += count[j];
            }
        }
    }
    let res = 0;
    const maxlen = Math.max(...dp);
    for (let i = 0; i < dp.length; i++) {
        if (dp[i] === maxlen) {
            res += count[i];
        }
    }
    return res;
}
