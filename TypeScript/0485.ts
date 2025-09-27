class Solution {
  findMaxConsecutiveOnes(nums: number[]): number {
    let cnt = 0;   // current streak of ones
    let res = 0;   // maximum streak found

    for (let i = 0; i < nums.length; i++) {
      if (nums[i] === 1) {
        cnt++;
        res = Math.max(res, cnt);
      } else {
        cnt = 0; // reset streak
      }
    }
    return res;
  }
}

const sol = new Solution();
console.log(sol.findMaxConsecutiveOnes([1,0,1,1,0,1]))