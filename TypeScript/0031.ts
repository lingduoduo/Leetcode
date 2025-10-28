/**
 Do not return anything, modify nums in-place instead.
 */
function nextPermutation(nums: number[]): void {
    let n = nums.length;
    for (let i = n - 2; i >= 0; i--) {
        if (nums[i] >= nums[i + 1]) continue;

        for (let j = n - 1; j >= i; j--) {
            if (nums[j] > nums[i]) {
                let tmp = nums[j];
                nums[j] = nums[i];
                nums[i] = tmp;
                break;
            }
        }
        let left = i + 1;
        let right = n - 1;
        while (left < right) {
            let tmp = nums[left];
            nums[left] = nums[right]
            nums[right] = tmp;
            left += 1;
            right -= 1;
        }
        return;
    }
    nums.reverse();
}