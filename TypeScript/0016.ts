function threeSumClosest(nums: number[], target: number): number {
  nums.sort((a, b) => a - b);
  // Track the closest SUM (not the diff). Initialize with any valid triple.
  let res = nums[0] + nums[1] + nums[2];

  for (let i = 0; i < nums.length - 2; i++) {
    let j = i + 1;
    let k = nums.length - 1;

    while (j < k) {
      const sum = nums[i] + nums[j] + nums[k];

      // Update if this sum is closer to target
      if (Math.abs(sum - target) < Math.abs(res - target)) {
        res = sum;
      }

      if (sum === target) return target;   // exact match
      if (sum < target) j++;               // need a larger sum
      else k--;                            // need a smaller sum
    }
  }
  return res;
}