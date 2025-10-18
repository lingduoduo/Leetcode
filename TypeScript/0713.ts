function numSubarrayProductLessThanK(nums: number[], k: number): number {
    if (k <=1) return 0;

    let cur = 1;
    let res = 0;
    let left = 0;

    for (let right = 0; right < nums.length; right++){
        cur = cur * nums[right];
        while (cur >= k && left <= right) {
            cur = cur / nums[left];
            left++;
        }
        res += right - left + 1;
    }
    return res;
};