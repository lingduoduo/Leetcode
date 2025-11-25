function rob(nums: number[]): number {
    if (nums.length === 0) {
        return 0;
    }
    if (nums.length === 1) {
        return nums[0];
    }

    const helper = (vals: number[]): number => {    
        if (vals.length === 0) {
            return 0;
        }
        if (vals.length === 1) {
            return vals[0];
        }
        const dp: number[] = new Array(vals.length).fill(0);
        dp[0] = vals[0];
        dp[1] = Math.max(vals[0], vals[1]);
        for (let i = 2; i < vals.length; i++) {
            dp[i] = Math.max(dp[i - 1], dp[i - 2] + vals[i]);
        }
        return dp[dp.length - 1];
    };

    const odds = helper(nums.slice(0, nums.length - 1));
    const evens = helper(nums.slice(1));
    return Math.max(odds, evens);   
    
};
