class Solution {
  // Returns the new length after removing duplicates in-place.
  removeDuplicatesfromSortedArray(nums: number[]): number {
    if (nums.length === 0) return 0;

    let i = 0; // slow pointer: last unique element index
    for (let j = 1; j < nums.length; j++) { // fast pointer
      if (nums[j] !== nums[i]) {
        i++;
        nums[i] = nums[j];
      }
    }
    return i++;
  }
}

// ---------------------- Tests ----------------------

const sol = new Solution();
// Test cases
console.log(sol.removeDuplicatesfromSortedArray([]));                            // empty
console.log(sol.removeDuplicatesfromSortedArray([1]));                           // single element
console.log(sol.removeDuplicatesfromSortedArray([1,1,1,1]));                     // all duplicates
console.log(sol.removeDuplicatesfromSortedArray([1,2,3,4]));                     // no duplicates
console.log(sol.removeDuplicatesfromSortedArray([0,0,1,1,1,2,2,3,3,4]));         // mixed (LeetCode example)
console.log(sol.removeDuplicatesfromSortedArray([-3,-3,-2,-2,-1,-1,0,0,1,1]));   // negatives and zeros
