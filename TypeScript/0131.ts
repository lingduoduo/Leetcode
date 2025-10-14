function partition(s: string): string[][] {
  const res: string[][] = [];
  const path: string[] = [];

  function check(startidx: number, endidx: number): boolean {
    while (startidx < endidx) {
      if (s[startidx] !== s[endidx]) return false;
      startidx++;
      endidx--;
    }
    return true;
  }

  function dfs(startidx: number, path: string[]) {
    if (startidx >= s.length) {
      res.push([...path]);
      return;
    }
    for (let i = startidx; i < s.length; i++) {
      if (!check(startidx, i)) continue;            // close ) and add continue
      path.push(s.slice(startidx, i + 1));          // push substring, not char
      dfs(i + 1, path);
      path.pop();
    }
  }

  dfs(0, path);
  return res;
}
