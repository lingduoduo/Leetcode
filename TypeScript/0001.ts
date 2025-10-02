class Solution {
  twoSum(nums: number[], target: number): number[] {
    const seen = new Map<number, number>(); // value -> index

    for (let i = 0; i < nums.length; i++) {
      const need = target - nums[i];
      if (seen.has(need)) {
        return [seen.get(need)!, i];
      }
      seen.set(nums[i], i);
    }
    return []; // or throw new Error("No solution");
  }
}

// quick checks
const sol = new Solution();
console.log(sol.twoSum([2,7,11,15], 9)); // [0,1]
console.log(sol.twoSum([3,2,4], 6));     // [1,2]
console.log(sol.twoSum([3,3], 6));       // [0,1]