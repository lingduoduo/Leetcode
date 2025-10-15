function findSubsequences(nums: number[]): number[][] {
  const res: number[][] = [];
  const n = nums.length;

  function dfs(idx: number, path: number[]): void {
    if (path.length >= 2) res.push([...path]);

    const used = new Set<number>(); // de-dup at this depth
    for (let i = idx; i < n; i++) {
      if (used.has(nums[i])) continue;                               // avoid same value at this level
      if (path.length > 0 && nums[i] < path[path.length - 1]) continue; // enforce non-decreasing

      used.add(nums[i]);
      path.push(nums[i]);
      dfs(i + 1, path);
      path.pop();
    }
  }

  dfs(0, []);
  return res;
}