function search(nums: number[], target: number): number {
    let mid: number, left: number = 0, right: number = nums.length;
    while (left < right) {

        mid = left +((right - left) >> 1);
        if (nums[mid] > target) {
            right = mid;
        } else if (nums[mid] < target) {
            left = mid + 1;
        } else {
            return mid;
        }
    }
    return -1;
};

const nums: number[] = [1, 2, 3, 4, 5, 6];
const target: number = 3;
const result: number = search(nums, target);
console.log(result); // 2