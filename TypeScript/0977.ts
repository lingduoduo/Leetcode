class Solution {
  sortedSquares(nums: number[]): number[] {
    const res: number[] = [];
    let left = 0,
        right = nums.length - 1;

    while (left <= right) {
      if (Math.abs(nums[left]) > Math.abs(nums[right])) {
        res.unshift(nums[left] ** 2);
        left++;
      } else {
        res.unshift(nums[right] ** 2);
        right--;
      }
    }

    return res;
  }
}

// Example usage:
const sol = new Solution();
console.log(sol.sortedSquares([-7, -3, 2, 3, 11])); // [4, 9, 9, 49, 121]
