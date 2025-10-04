class Solution {
  fourSumCount(
    nums1: number[],
    nums2: number[],
    nums3: number[],
    nums4: number[]
  ): number {
    const sum12 = new Map<number, number>();

    // Count all sums of nums1[i] + nums2[j]
    for (let i = 0; i < nums1.length; i++) {
      for (let j = 0; j < nums2.length; j++) {
        const s = nums1[i] + nums2[j];
        sum12.set(s, (sum12.get(s) ?? 0) + 1);
      }
    }

    // For each sum in nums3[k] + nums4[l], look for its negation in sum12
    let res = 0;
    for (let k = 0; k < nums3.length; k++) {
      for (let l = 0; l < nums4.length; l++) {
        const s = nums3[k] + nums4[l];
        const need = -s;
        const freq = sum12.get(need);
        if (freq) res += freq;
      }
    }
    return res;
  }
}
