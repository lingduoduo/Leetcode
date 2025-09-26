class Solution {
  minSubArrayLen(target: number, nums: number[]): number {
    if (target <= 0) return 0;

    let left = 0;
    let sum = 0;
    let res = Infinity;

    for (let right = 0; right < nums.length; right++) {
      sum += nums[right];

      while (sum >= target) {
        res = Math.min(res, right - left + 1);
        sum -= nums[left];
        left += 1;
      }
    }

    return res === Infinity ? 0 : res;
  }
}

// ✅ Test cases
const sol = new Solution();
console.log(sol.minSubArrayLen(7, [2,3,1,2,4,3]));  // 2  -> [4,3]
console.log(sol.minSubArrayLen(15, [1,2,3,4,5]));   // 5  -> [1,2,3,4,5]
console.log(sol.minSubArrayLen(4, [1,4,4]));        // 1  -> [4]
console.log(sol.minSubArrayLen(11, [1,2,3,4,5]));   // 3  -> [3,4,5] = 12
console.log(sol.minSubArrayLen(100, [1,2,3]));      // 0  -> none
console.log(sol.minSubArrayLen(7, []));             // 0
console.log(sol.minSubArrayLen(0, [1,2,3]));        // 0
