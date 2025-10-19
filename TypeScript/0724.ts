function pivotIndex(nums: number[]): number {
    let tot = nums.reduce((a, b) => a+b);
    let cur = 0;
    for (let i = 0; i < nums.length; i++){
        if (cur * 2 + nums[i] === tot) return i;
        cur += nums[i];
    }
    return -1;
};