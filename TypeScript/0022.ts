function generateParenthesis(n: number): string[] {
  const res: string[] = [];

  function dfs(left: number, right: number, path: string): void {
    if (left === 0 && right === 0) {
      res.push(path);
      return;
    }

    if (left > 0) {
      dfs(left - 1, right, path + "(");
    }

    if (right > left) {
      dfs(left, right - 1, path + ")");
    }
  }

  dfs(n, n, "");
  return res;
}
