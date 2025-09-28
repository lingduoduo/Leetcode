class Solution {
  applyOperations(nums: number[]): number[] {
    const n = nums.length;

    // Phase 1: apply operations left-to-right
    for (let i = 0; i < n - 1; i++) {
      if (nums[i] === nums[i + 1]) {
        nums[i] *= 2;
        nums[i + 1] = 0;
      }
    }

    // Phase 2: move zeros to the end (stable)
    let idx = 0; // next position for a non-zero
    for (let i = 0; i < n; i++) {
      if (nums[i] !== 0) {
        if (i !== idx) {
          [nums[idx], nums[i]] = [nums[i], nums[idx]];
        }
        idx++;
      }
    }
    return nums;
  }
}

const sol = new Solution();
console.log(sol.applyOperations([1,2,2,1,1,0]))