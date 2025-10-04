class Solution {
  threeSum(nums: number[]): number[][] {
    const res: number[][] = [];
    nums.sort((a, b) => a - b); // numeric sort

    for (let i = 0; i < nums.length - 2; i++) {
      if (i > 0 && nums[i] === nums[i - 1]) continue; // skip dup i

      let j = i + 1;
      let k = nums.length - 1;

      while (j < k) {
        const sum = nums[i] + nums[j] + nums[k];
        if (sum === 0) {
          res.push([nums[i], nums[j], nums[k]]);
          j++;
          k--;
          // skip dup j
          while (j < k && nums[j] === nums[j - 1]) j++;
          // skip dup k
          while (j < k && nums[k] === nums[k + 1]) k--;
        } else if (sum < 0) {
          j++;
        } else {
          k--;
        }
      }
    }
    return res;
  }
}
