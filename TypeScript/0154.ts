function findMin(nums: number[]): number {
    let left = 0;
    let right = nums.length - 1;

    while (left < right) {
        // skip duplicates on the left
        while (left < right && nums[left] === nums[left + 1]) {
            left++;
        }
        // skip duplicates on the right
        while (left < right && nums[right] === nums[right - 1]) {
            right--;
        }

        // after skipping duplicates, it's possible left == right
        if (left === right) break;

        const mid = left + Math.floor((right - left) / 2);

        if (nums[mid] < nums[right]) {
            right = mid;
        } else {
            left = mid + 1;
        }
    }

    return nums[left];
}
