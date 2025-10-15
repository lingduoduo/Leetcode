function subsets(nums: number[]): number[][] {
  nums.sort((a, b) => a - b);

  const res: number[][] = [];
  const n = nums.length;

  function dfs(idx: number, path: number[]): void {
    res.push([...path]); // record current subset

    for (let i = idx; i < n; i++) {
      // skip duplicates at the same tree level
      if (i > idx && nums[i] === nums[i - 1]) continue;
      path.push(nums[i]);
      dfs(i + 1, path);
      path.pop();
    }
  }

  dfs(0, []);
  return res;
}
