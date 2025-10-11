function searchInsert(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length;
    while (left < right) {
        const mid = left + Math.floor((right - left) / 2);
        if (nums[mid] == target) {
            return mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            right = mid;
        }
    }
    return right;
};