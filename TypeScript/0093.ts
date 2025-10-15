function restoreIpAddresses(s: string): string[] {
  const res: string[] = [];

  function check(start: number, end: number): boolean {
    if (start > end) return false;
    // no leading zeros unless the segment is exactly "0"
    if (s[start] === "0" && start !== end) return false;
    const num = parseInt(s.slice(start, end + 1), 10); // end is inclusive
    return 0 <= num && num <= 255;
  }

  function dfs(idx: number, path: string[]) {
    if (idx === s.length && path.length === 4) {
      res.push(path.join("."));
      return;
    }
    if (path.length >= 4) return;

    // try segments of length 1..3 (end is inclusive)
    for (let i = idx; i <= Math.min(s.length - 1, idx + 2); i++) {
      if (check(idx, i)) {
        const sub = s.slice(idx, i + 1);
        path.push(sub);
        dfs(i + 1, path);
        path.pop();
      }
    }
  }

  dfs(0, []);
  return res;
};