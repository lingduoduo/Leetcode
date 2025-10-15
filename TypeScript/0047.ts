function permuteUnique(nums: number[]): number[][] {
  const res: number[][] = [];
  const used: boolean[] = new Array(nums.length).fill(false);
  nums.sort((a, b) => a - b); // sort so duplicates are adjacent

  function dfs(path: number[]): void {
    if (path.length === nums.length) {
      res.push([...path]);
      return;
    }

    for (let i = 0; i < nums.length; i++) {
      if (used[i]) continue;                                  // already used this index
      if (i > 0 && nums[i] === nums[i - 1] && !used[i - 1]) continue; // skip dup at this level

      used[i] = true;
      path.push(nums[i]);
      dfs(path);
      path.pop();
      used[i] = false;
    }
  }

  dfs([]);
  return res;
}