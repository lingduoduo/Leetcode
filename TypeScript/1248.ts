function numberOfSubarrays(nums: number[], k: number): number {
  let res = 0;
  const d = new Map<number, number>();
  d.set(0, 1);

  let presum = 0;
  for (const x of nums) {                 // use values, not indexes
    if ((x & 1) === 1) presum++;          // odd -> increment prefix of odds

    const need = presum - k;
    res += d.get(need) ?? 0;              // add counts of needed prefix

    d.set(presum, (d.get(presum) ?? 0) + 1);
  }
  return res;
}