// leetcode_26_remove_duplicates.ts

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
    return i + 1;
  }
}

// ---------------------- Tests ----------------------

function runCase(input: number[]) {
  const sol = new Solution();
  const arr = [...input]; // copy so we can show original
  const k = sol.removeDuplicatesfromSortedArray(arr);
  console.log(`input:  ${JSON.stringify(input)}`);
  console.log(`k:      ${k}`);
  console.log(`output: ${JSON.stringify(arr.slice(0, k))}`);
  console.log("-".repeat(40));
}

// Test cases
runCase([]);                            // empty
runCase([1]);                           // single element
runCase([1,1,1,1]);                     // all duplicates
runCase([1,2,3,4]);                     // no duplicates
runCase([0,0,1,1,1,2,2,3,3,4]);         // mixed (LeetCode example)
runCase([-3,-3,-2,-2,-1,-1,0,0,1,1]);   // negatives and zeros
