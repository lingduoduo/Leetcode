function permute(nums: number[]): number[][] {
  const res: number[][] = [];

  function dfs(sub: number[], path: number[]): void {
    if (sub.length === 0) {
      res.push([...path]);
      return;
    }

    for (let i = 0; i < sub.length; i++) {
      const cur = sub[i];
      const next = sub.slice(0, i).concat(sub.slice(i + 1)); // remove sub[i]
      path.push(cur);
      dfs(next, path);
      path.pop();
    }
  }

  dfs(nums, []);
  return res;
}