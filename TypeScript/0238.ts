function productExceptSelf(nums: number[]): number[] {
  const n = nums.length;
  const pre = Array(n + 1).fill(1);   // pre[i] = product of nums[0..i-1]
  const post = Array(n + 1).fill(1);  // post[i] = product of nums[i..n-1]

  // build prefix
  for (let i = 1; i <= n; i++) {
    pre[i] = pre[i - 1] * nums[i - 1];
  }

  // build suffix
  for (let i = n - 1; i >= 0; i--) {
    post[i] = post[i + 1] * nums[i];
  }

  // combine: product except self at i = pre[i] * post[i+1]
  const res = Array(n);
  for (let i = 0; i < n; i++) {
    res[i] = pre[i] * post[i + 1];
  }
  return res;
}
