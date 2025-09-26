class Solution {
  // 704. Binary Search
  search(nums: number[], target: number): number {
    let left = 0;
    let right = nums.length - 1;

    while (left <= right) {
      const mid = Math.floor((left + right) / 2);

      if (nums[mid] === target) {
        return mid; // found target
      } else if (nums[mid] < target) {
        left = mid + 1; // search right half
      } else {
        right = mid - 1; // search left half
      }
    }
    return -1; // not found
  }
}

// Example usage:
const sol = new Solution();
const nums = [-10, -3, 0, 5, 9, 12, 18];
console.log(sol.search(nums, 9));   // 4
console.log(sol.search(nums, -3));  // 1
console.log(sol.search(nums, 7));   // -1
