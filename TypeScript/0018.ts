class Solution {
  fourSum(nums: number[], target: number): number[][] {
    const res: number[][] = [];
    const n = nums.length;
    if (n < 4) return res;

    nums.sort((a, b) => a - b);

    for (let i = 0; i < n - 3; i++) {
      if (i > 0 && nums[i] === nums[i - 1]) continue; // skip dup i

      for (let j = i + 1; j < n - 2; j++) {
        if (j > i + 1 && nums[j] === nums[j - 1]) continue; // skip dup j

        let k = j + 1;
        let l = n - 1;

        while (k < l) {
          const sum = nums[i] + nums[j] + nums[k] + nums[l];

          if (sum === target) {
            res.push([nums[i], nums[j], nums[k], nums[l]]);
            k++;
            l--;
            // skip dup k
            while (k < l && nums[k] === nums[k - 1]) k++;
            // skip dup l
            while (k < l && nums[l] === nums[l + 1]) l--;
          } else if (sum < target) {
            k++;
          } else {
            l--;
          }
        }
      }
    }

    return res;
  }
}
