function subsets(nums: number[]): number[][] {
  const res: number[][] = [];
  const n = nums.length;

  function dfs(idx: number, path: number[]): void {
    res.push([...path]); // record current subset

    for (let i = idx; i < n; i++) {
      path.push(nums[i]);
      dfs(i + 1, path);
      path.pop();
    }
  }

  dfs(0, []);
  return res;
}
