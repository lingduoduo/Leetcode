function largestSumAfterKNegations(nums: number[], k: number): number {
     nums.sort((a, b) => Math.abs(b) - Math.abs(a));

    for (let i=0; i<nums.length && k > 0; i++){
        if (nums[i] < 0){
            nums[i] = -nums[i];
            k--;
        }
    }
    if (k % 2 === 1)
        nums[nums.length-1] = -nums[nums.length-1];

    const res = nums.reduce((s, x) => s + x, 0);
    return res;
};