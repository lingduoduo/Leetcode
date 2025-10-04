class Solution {
  containsNearbyDuplicate(nums: number[], k: number): boolean {
    const lastIndex = new Map<number, number>();

    for (let i = 0; i < nums.length; i++) {
      const v = nums[i];
      const prev = lastIndex.get(v);
      if (prev !== undefined && i - prev <= k) return true;
      lastIndex.set(v, i);
    }
    return false;
  }
}