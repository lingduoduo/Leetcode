function canJump(nums: number[]): boolean {
    let res = 0;
    let cur = 0;

    for (let i = 0; i< nums.length; i++){
        if (res < i) return false;
        res = Math.max(res, i + nums[i]);
    }
    return true;
};