class Solution {
  moveZeroes(nums: number[]): void {
    let idx = 0; // position to place next non-zero

    for (let i = 0; i < nums.length; i++) {
      if (nums[i] !== 0) {
            [nums[idx], nums[i]] = [nums[i], nums[idx]];
            idx++;
      }
    }
  }
}

// Example usage
const sol = new Solution();
let arr = [0, 1, 0, 3, 12];
sol.moveZeroes(arr);
console.log(arr);  // [1, 3, 12, 0, 0]