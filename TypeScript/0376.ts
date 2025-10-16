function wiggleMaxLength_alt(nums: number[]): number {
  if (nums.length <= 1) return nums.length;

  let prevDiff = 0;
  let res = 1; // at least one element

  for (let i = 1; i < nums.length; i++) {
    const diff = nums[i] - nums[i - 1];
    if (diff === 0) continue;
    if ((diff > 0 && prevDiff <= 0) || (diff < 0 && prevDiff >= 0)) {
      res++;
      prevDiff = diff;
    }
  }
  return res;
}
